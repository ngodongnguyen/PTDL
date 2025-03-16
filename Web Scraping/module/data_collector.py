import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
from unidecode import unidecode
import os

# Đường dẫn tới ChromeDriver
# chromedriver_path = "D:/APP/chromedriver/chromedriver.exe"

# Cấu hình ChromeDriver service
# service = webdriver.ChromeService(chromedriver_path)

options = webdriver.ChromeOptions()

# Cấu hình để web không cần load hình ảnh
chrome_prefs = {
    "profile.default_content_setting_values": {
        "images": 2,
    }
}
options.experimental_options["prefs"] = chrome_prefs
# Chạy ẩn danh (không hiển thị trình duyệt)
options.add_argument("--headless=new")
# Một số hệ thống check user-agent và không cho headless-chrome chạy nên phải thêm user-agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument("--disable-gpu")  # Tắt GPU (không cần thiết cho chế độ headless)
def getdata(link: str) -> dict:
    # Tạo instance của trình điều khiển Chrome
    driver = webdriver.Chrome(options=options)
    
    # Mở trang web        
    driver.get(link)


    try:
        # Tìm nút "Xem thêm"
        xem_them_button = driver.find_element(By.CSS_SELECTOR, 'button.b1wrxwj6.outline.o-tertiary.r-normal.medium.w-bold')

        # Cuộn trang xuống thêm 300px để đảm bảo nút không bị che khuất bởi quảng cáo
        driver.execute_script("window.scrollBy(0, 1000);")  # Cuộn trang thêm 300px xuống dưới
        

        # Bấm nút "Xem thêm" lần 1
        actions = ActionChains(driver)
        actions.move_to_element(xem_them_button).click().perform()


        # Bấm nút "Xem thêm" lần 2 để chắc chắn quảng cáo đã tắt
        actions.move_to_element(xem_them_button).click().perform()
        
        # Đợi để nội dung mới tải xong
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.a13uoc2z'))  # Kiểm tra bảng thuộc tính đã tải xong
        )
    except Exception as e:
        print(f"Không tìm thấy hoặc không thể bấm nút 'Xem thêm': {e}")
    

    # Lấy nội dung HTML của trang sau khi quảng cáo đã tắt
    html_text = driver.page_source
    driver.quit()

    # Phân tích HTML để trích xuất dữ liệu
    soup = BeautifulSoup(html_text, 'html.parser')
    item = {}

    # Lấy địa chỉ, xử lý trường hợp không có địa chỉ
    try:
        item['DiaChi'] = soup.find('span', class_='bwq0cbs flex-1').text
    except AttributeError:
        item['DiaChi'] = None  # Nếu không có địa chỉ, gán None

    # Chọn bảng chứa thuộc tính để lấy dữ liệu
    attrTable = soup.find('div', class_='a13uoc2z')
    
    if attrTable:  # Kiểm tra nếu bảng thuộc tính tồn tại
        
        # Lấy tất cả các thuộc tính từ các div có lớp 'col-xs-6 abzctes'
        attrStrings = attrTable.find_all('div', class_='col-xs-6 abzctes')

        # Lặp qua các thuộc tính và trích xuất dữ liệu
        for attr in attrStrings:
            key = attr.find('span').text.strip()  # Lấy tên thuộc tính
            value = attr.find('strong').text.strip()  # Lấy giá trị thuộc tính
            
            
            item[unidecode(key.title().replace(' ', ''))] = value


    return item
def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def savedata(links, getdata):

    data_list = []
    
    # Lặp qua từng link và thu thập dữ liệu
    for i, link in enumerate(links):
        data = getdata(link)  # Gọi hàm getdata để thu thập dữ liệu
        if data:
            data_list.append(data)

        # Mỗi 100 link thì lưu vào một file JSON
        if (i + 1) % 100 == 0:
            filename = f"data_{(i + 1) // 100}.json"  # Tạo tên file cho mỗi 100 link
            save_to_json(data_list, filename)
            print(f"Đã lưu {filename} với {len(data_list)} mục.")
            data_list = []  # Reset danh sách dữ liệu để tiếp tục

    # Đảm bảo lưu tất cả dữ liệu còn lại vào file JSON cuối cùng nếu có
    if data_list:
        filename = f"data_{(i + 1) // 100 + 1}.json"
        save_to_json(data_list, filename)
        print(f"Đã lưu {filename} với {len(data_list)} mục.")
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_product_links(n):
    # Cấu hình trình duyệt
    baseUrl = "https://www.nhatot.com/mua-ban-dat?page="
    linkSelector = "a.crd7gu7"
    arr = []

    try:
        # Lặp qua các trang từ 1 đến n
        for pageNum in range(n, n+100):
            driver = webdriver.Chrome(options=options)
            # Mở trang web
            url = baseUrl + str(pageNum)
            print(f"Đang lấy dữ liệu từ trang: {url}")
            driver.get(url)

            # Lấy tất cả các đường link sản phẩm
            links = driver.find_elements(By.CSS_SELECTOR, linkSelector)

            for link in links:
                arr.append(link.get_attribute('href'))

            # Đóng trình duyệt sau khi lấy dữ liệu từ một trang
            driver.close()
            driver.quit()
    except Exception as e:
        print(f"Có lỗi xảy ra: {str(e)}")
    df = pd.DataFrame(arr, columns=['links'])
    return df


