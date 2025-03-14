import cloudscraper
from bs4 import BeautifulSoup
from unidecode import unidecode
import re
from time import sleep
import random
from datetime import datetime
import traceback
import common


def get_current_time_str():
    current_datetime = datetime.now()
    return current_datetime.strftime("%d_%m_%Y_%H_%M")


def extract_page_in_url(url: str):
    return url.rsplit("/", 1)[-1]


def extract_coordinates(html_content):
    pattern = r"place\?q=([-+]?\d*\.\d+),([-+]?\d*\.\d+)"
    match = re.search(pattern, html_content)
    if match:
        return [float(match.group(1)), float(match.group(2))]
    return [None, None]


def extract_property_urls(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    base_url = "https://batdongsan.com.vn"
    return [
        base_url + element.get("href")
        for element in soup.select(".js__product-link-for-product-id")
    ]


def process_single_property(property_url, scraper: cloudscraper.CloudScraper):
    response = scraper.get(property_url)

    if response.status_code != 200:
        return None

    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    property_data = {}

    # Lấy thông tin bất động sản
    elements = soup.find_all("div", class_="re__pr-specs-content-item")
    for item in elements:
        key_tag = item.find("span", class_="re__pr-specs-content-item-title")
        value_tag = item.find("span", class_="re__pr-specs-content-item-value")
        if key_tag and value_tag:
            key = key_tag.text.strip()
            value = value_tag.text.strip()
            property_data[unidecode(key.title().replace(" ", ""))] = value

    # Địa chỉ bất động sản
    address_tag = soup.find("span", class_="re__pr-short-description js__pr-address")
    property_data["DiaChi"] = address_tag.text.strip() if address_tag else None

    # Thành phố, Quận/Huyện
    breadCrumb_addr = soup.select(
        "div.re__breadcrumb.js__breadcrumb.js__ob-breadcrumb .re__link-se"
    )
    property_data["City"] = breadCrumb_addr[1].text.strip() if len(breadCrumb_addr) > 1 else None
    property_data["District"] = breadCrumb_addr[2].text.strip() if len(breadCrumb_addr) > 2 else None

    # Tọa độ bản đồ
    map_coor_tag = soup.find("div", class_="re__section re__pr-map js__section js__li-other")
    map_coor = extract_coordinates(str(map_coor_tag))
    property_data["Lat"], property_data["Long"] = map_coor

    return property_data


def process_single_page(page_url, scraper):
    print("Processing:", page_url)
    response = scraper.get(page_url)
    if response.status_code != 200:
        return []

    properties = []
    prop_urls = extract_property_urls(response.text)
    for prop_url in prop_urls:
        prop_data = process_single_property(prop_url, scraper)
        if prop_data:
            properties.append(prop_data)
        sleep(random.randint(1, 3))

    return properties


def process_multiple_pages(fileOutPath, base_url, start, end, typeOfProperty="batdongsan"):
    scraper = cloudscraper.create_scraper(
        delay=30, browser={"browser": "chrome", "platform": "windows", "mobile": False}
    )
    temp = []
    prev = start
    i = start
    try:
        for i in range(start, end + 1):
            temp += process_single_page(base_url + str(i), scraper)

            # Ghi file sau mỗi 100 trang
            if i % 100 == 0:
                common.write_json_file(fileOutPath, temp, prev, i, typeOfProperty)
                prev = i + 1
                temp.clear()
    except Exception as e:
        print(f"Lỗi tại trang: {base_url + str(i)} !!!! {e}")
        print(traceback.format_exc())  # In ra toàn bộ lỗi
    finally:
        if temp:
            common.write_json_file(fileOutPath, temp, prev, i, typeOfProperty)
