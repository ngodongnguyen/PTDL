import pandas as pd
def chuyen_chieu_ngang_hoac_chieu_dai_sang_m(x):
    if not isinstance(x, str): #nếu giá trị không phải chuỗi (str), ví dụ là NaN, None thì hàm sẽ trả về None
        return None
    x = x.replace(',', '.').strip()  # Chuẩn hóa: thay dấu phẩy thành dấu chấm

    if 'm' in x:  # Nếu có chữ 'm'
        try:
            return float(x.replace('m', '').strip())  # Chuyển đổi giá trị sau khi xóa 'm'
        except:
            return None  # Nếu có lỗi thì trả về None
    else:
        return None  # Nếu không có 'm', trả về None
def chuyen_hoa(row):
    chieuDai = row['ChieuDai']
    chieuNgang = row['ChieuNgang']
    dienTich = row['DienTichDat']
    dienTich = float(dienTich.replace(',', '.')) if isinstance(dienTich, str) else dienTich

    if pd.isna(chieuDai) and pd.isna(chieuNgang):
        chieuDai = float(round(dienTich / 2,2))
        chieuNgang = float(round(dienTich / 2,2))
    # Nếu chỉ có chiều dài NaN và chiều ngang có dữ liệu
    elif pd.isna(chieuDai) and pd.notna(chieuNgang):
        chieuDai = float(round(dienTich / chieuNgang,2))
    # Nếu chỉ có chiều ngang NaN và chiều dài có dữ liệu
    elif pd.isna(chieuNgang) and pd.notna(chieuDai):
        chieuNgang = float(round(dienTich / chieuDai,2))
    # Trường hợp không có NaN, giữ nguyên
    return pd.Series([chieuDai, chieuNgang])


def chuyen_dien_tich_sang_m2(x):
    if not isinstance(x, str): #nếu giá trị không phải chuỗi (str), ví dụ là NaN, None thì hàm sẽ trả về None
        return None
    x = x.replace(',', '.').strip() # thay đổi phẩy thành chấm

    if 'm²' in x:
        return float(x.replace('m²', '').strip())
    elif 'hecta' in x:
        so = float(x.replace('hecta', '').strip())
        return so * 10000
    else:
        return None  
def chuyen_hoa_loai_hinh_dat(x):
    if not isinstance(x, str): #nếu giá trị không phải chuỗi (str), ví dụ là NaN, None thì hàm sẽ trả về None
        return None
    if x=='Đất thổ cư':
        return 0
    elif x=='Đất nông nghiệp':
        return 1
    elif x=='Đất nền dự án':
        return 2
    elif x=='Đất công nghiệp':
        return 3
    else:
        return None
def chuyen_hoa_giay_to_phap_ly(x):
    if not isinstance(x, str):  # Nếu giá trị không phải chuỗi (str), ví dụ NaN, None thì hàm trả về None
        return None
#     GiayToPhapLy
# Đã có sổ                         16544
# Đang chờ sổ                        259
# Sổ chung / công chứng vi bằng      103
# Giấy tờ viết tay                    55
# Không có sổ                         11
# 3                                    3
    if x == 'Đã có sổ' or x=='3':
        return 0  # Trả về 0 kiểu int
    elif x == 'Đang chờ sổ':
        return 1  # Trả về 1 kiểu int
    elif x == 'Sổ chung / công chứng vi bằng':
        return 2  # Trả về 2 kiểu int
    elif x == 'Giấy tờ viết tay':
        return 3  # Trả về 3 kiểu int
    elif x == "Không có sổ":
        return 4  # Trả về 4 kiểu int
    else:
        return None  # Trả về None nếu không khớp với bất kỳ giá trị nào
import unidecode

def chuyen_hoa_huong_dat(x):
    if not isinstance(x, str):  # Nếu giá trị không phải chuỗi (str), ví dụ NaN, None thì hàm trả về None
        return 0
    
    # Loại bỏ dấu và chuyển thành chữ hoa để chuẩn hóa dữ liệu
    x = unidecode.unidecode(x).upper()

    if x == "DONG NAM":
        return 1
    elif x == 'DONG BAC':
        return 2
    elif x == "TAY BAC":
        return 3
    elif x == "TAY NAM":
        return 4
    elif x == "DONG":
        return 5
    elif x == "NAM":
        return 6
    elif x == "TAY":
        return 7
    elif x == "BAC":
        return 8
    return 0  # Nếu không phải các hướng trong danh sách
def convert_to_trieu(x):
    # Kiểm tra nếu giá trị không phải là chuỗi, trả về 0
    if not isinstance(x, str):
        return 0
    
    # Loại bỏ dấu và chuyển thành chữ hoa
    x = unidecode.unidecode(x).upper()
    
    # Tách phần sau dấu '/'
    unit = x.split('/')[0].strip().split(' ')[1]  # Lấy phần sau dấu '/' và loại bỏ khoảng trắng
    value=x.split('/')[0].strip().split(' ')[0]
    # Tách phần số
    value = value.replace(',', '.')

    value = float(value)  # Chuyển giá trị thành số
    
    # Chuyển đổi theo đơn vị
    if 'TRIEU' == unit:
        return value  # Đã là triệu, không cần chuyển đổi
    elif 'TY' in unit:
        return value * 1000  # 1 tỷ = 1,000 triệu
    elif 'D' in unit:
        return value / 1000000  # 1 triệu = 1,000,000 đ
    return 0  # Nếu không có đơn vị hợp lệ, trả về 0
def tach_dia_chi(dia_chi):
    if not isinstance(dia_chi, str):
        return None
    dia_chi = dia_chi.replace("Tp Hồ Chí Minh", "Thành phố Hồ Chí Minh")
    dia_chi = dia_chi.replace('Thừa Thiên Huế', 'Thành phố Huế')


    dia_chi_parts = [part.strip() for part in dia_chi.split(',')]

    # Kiểm tra nếu có đủ 4 phần (Thành Phố, Quận, Phường, Thông tin thêm)
    if len(dia_chi_parts) >= 4:
        thanh_pho_tinh = dia_chi_parts[-1]  # Thành phố/Tỉnh
        quan_huyen = dia_chi_parts[-2]      # Quận/Huyện
        phuong_xa = dia_chi_parts[-3]       # Phường/Xã
        thong_tin_them = ', '.join(dia_chi_parts[:-3])  # Các thông tin còn lại
    elif len(dia_chi_parts) == 3:
        thanh_pho_tinh = dia_chi_parts[-1]  # Thành phố/Tỉnh
        quan_huyen = dia_chi_parts[-2]      # Quận/Huyện
        phuong_xa = ', '.join(dia_chi_parts[:-2])
        thong_tin_them = ""  # Các thông tin còn lại
    elif len(dia_chi_parts) == 2:
        thanh_pho_tinh = dia_chi_parts[-1]  # Thành phố/Tỉnh
        quan_huyen = dia_chi_parts[0]
        phuong_xa = ""
        thong_tin_them = ""  # Các thông tin còn lại
    else:
        thanh_pho_tinh = dia_chi_parts[0]
        quan_huyen = ""
        phuong_xa = ""
        thong_tin_them = ""

    return {
        "Thành Phố / Tỉnh": thanh_pho_tinh,
        "Quận / Huyện": quan_huyen,
        "Phường / Xã": phuong_xa,
        "Thông Tin Thêm": thong_tin_them
    }
import json

# Đọc file JSON chứa thông tin về tỉnh, quận, phường
with open('../data/DonViHanhChinh.json', 'r', encoding='utf-8') as f:
    donvihanhchinh = json.load(f)
import unicodedata
def so_hoa_thanh_pho(dia_chi_data):

    thanh_pho_tinh = dia_chi_data['Thành Phố / Tỉnh']
    if "Hòa Bình" in thanh_pho_tinh:
        # Chuẩn hóa tên thành phố, quận, phường chỉ khi là Hòa Bình
        thanh_pho_tinh = unicodedata.normalize('NFD', thanh_pho_tinh).encode('ascii', 'ignore').decode('utf-8').strip().upper()
    elif "Thừa Thiên Huế" in thanh_pho_tinh:
        # Nếu là Thừa Thiên Huế, thay thế thành Thành phố Huế
        thanh_pho_tinh = "Thành phố Huế"
    thanh_pho_tinh = thanh_pho_tinh.strip().upper()



    # Khởi tạo mã các cấp là 0
    ma_tinh = 0

    # Duyệt qua toàn bộ tỉnh
    for item in donvihanhchinh:
        # Kiểm tra Tỉnh/Thành phố
        if thanh_pho_tinh in item['Tỉnh / Thành Phố'].strip().upper() :
            ma_tinh = item['Mã Tỉnh']
            break
        else:
            if thanh_pho_tinh in unicodedata.normalize('NFD', item['Tỉnh / Thành Phố']).encode('ascii', 'ignore').decode('utf-8').strip().upper():
                ma_tinh = item['Mã Tỉnh']
                break
    # Nếu không tìm thấy mã nào, in cảnh báo
    if ma_tinh == 0:
        print(f"Cảnh báo: Không tìm thấy mã cho tỉnh {thanh_pho_tinh}")
    return {
        "Mã Tỉnh": ma_tinh,
    }
count=0
def so_hoa_quan(ma_tinh, quan_huyen):
    ma_quan = 0
    thay_the_quan = {
        "Thị xã Bến Cát": "Thành phố Bến Cát",
        "Thị xã Phú Mỹ": "Thành phố Phú Mỹ",
        "Huyện Chơn Thành": "Thị xã Chơn Thành",
        "Thị xã Tân Uyên": "Thành phố Tân Uyên",
        "Thị xã Từ Sơn": "Thành phố Từ Sơn",
        "Thành phố Qui Nhơn": "Thành phố Quy Nhơn",
        "Thành phố Tuy Hòa": "Thành phố Tuy Hoà",
        "Huyện Đất Đỏ": "Huyện Long Đất",
        "Huyện Long Điền": "Huyện Long Đất",
        "Huyện Hòa Thành": "Thị xã Hòa Thành",
        "Huyện Trảng Bàng": "Thị xã Trảng Bàng",
        "Huyện An Dương": "Quận An Dương",
        "Thị xã Gò Công": "Thành phố Gò Công",
        "Huyện Thuận Thành": "Thị xã Thuận Thành",
        "Huyện Đông Sơn":"Thành phố Thanh Hóa",
        "Huyện Đạ Tẻh":"Huyện Đạ Huoai",
        "Thị xã Đông Triều":"Thành phố Đông Triều",
        "Huyện Tịnh Biên":"Thị xã Tịnh Biên",
        "Huyện Thuỷ Nguyên":"Thành phố Thuỷ Nguyên",
        "Huyện Mộc Châu":"Thị xã Mộc Châu",
        "Thị xã Phổ Yên":"Thành phố Phổ Yên",
        "Huyện Kim Bảng":"Thị xã Kim Bảng",
        "Huyện Mỹ Lộc":"Thành phố Nam Định"
    }
    if quan_huyen in thay_the_quan:
        quan_huyen = thay_the_quan[quan_huyen]
        quan_huyen = unicodedata.normalize('NFD', quan_huyen).encode('ascii', 'ignore').decode('utf-8').strip().upper()
    if quan_huyen=="Huyện Phong Điền" and ma_tinh==46:
        quan_huyen="Thị xã Phong Điền"
        quan_huyen = unicodedata.normalize('NFD', quan_huyen).encode('ascii', 'ignore').decode('utf-8').strip().upper()
    for item in donvihanhchinh:
        if item['Mã Tỉnh'] == ma_tinh:
            for quan in item['Quận Huyện']:
                # Kiểm tra nếu là "Thị xã Bến Cát", thay thế thành "Thành phố Bến Cát"
                # Tìm quận/huyện khớp với giá trị sau khi thay thế
                if quan_huyen.strip().upper() in quan['Quận Huyện'].strip().upper():
                    ma_quan = quan['Mã Quận Huyện']
                    break  # Dừng lại khi tìm thấy quận
                else:
                    if quan_huyen in unicodedata.normalize('NFD', quan['Quận Huyện']).encode('ascii', 'ignore').decode('utf-8').strip().upper():
                        ma_quan = quan['Mã Quận Huyện']
                        break
            break  # Dừng lại khi tìm thấy tỉnh

    return ma_quan

def so_hoa_phuong(ma_tinh, ma_quan, phuong_xa):
    ma_phuong = 0
    thay_the_phuong = {
        "Phường Tăng Nhơn Phú A (Quận 9 cũ)": "Phường Tăng Nhơn Phú A",
        "Phường Tăng Nhơn Phú B (Quận 9 cũ)": "Phường Tăng Nhơn Phú B",
        "Phường Linh Trung (Quận Thủ Đức cũ)":"Phường Linh Trung",
        "Phường Bình Trưng Tây (Quận 2 cũ)":"Phường Bình Trưng Tây",
        "Phường Long Trường (Quận 9 cũ)":"Phường Long Trường",
        "Phường Linh Đông (Quận Thủ Đức cũ)":"Phường Linh Đông",
        "Phường Phước Long B (Quận 9 cũ)":"Phường Phước Long B",
        "Phường Bình Chiểu (Quận Thủ Đức cũ)":"Phường Bình Chiểu",
        "Phường An Phú (Quận 2 cũ)":"Phường An Phú",
        "Phường Linh Xuân (Quận Thủ Đức cũ)":"Phường Linh Xuân",
        "Phường Long Bình (Quận 9 cũ)":"Phường Long Bình",
        "Phường Long Thạnh Mỹ (Quận 9 cũ)":"Phường Long Thạnh Mỹ",
        "Phường Phú Hữu (Quận 9 cũ)":"Phường Phú Hữu",
        "Phường Hiệp Bình Phước (Quận Thủ Đức cũ)":"Phường Hiệp Bình Phước",
        "Phường Trường Thọ (Quận Thủ Đức cũ)":"Phường Trường Thọ",
        "Phường Phước Long A (Quận 9 cũ)":"Phường Phước Long A",
        "Phường Linh Chiểu (Quận Thủ Đức cũ)":"Phường Linh Chiểu",
        "Phường Phước Bình (Quận 9 cũ)":"Phường Phước Bình",
        "Phường Thạnh Mỹ Lợi (Quận 2 cũ)":"Phường Thạnh Mỹ Lợi",
        "Phường Hiệp Bình Chánh (Quận Thủ Đức cũ)":"Phường Hiệp Bình Chánh",
        "Phường Hiệp Phú (Quận 9 cũ)":"Phường Hiệp Phú",
        "Phường Tam Bình (Quận Thủ Đức cũ)":"Phường Tam Bình",
        "Phường Cát Lái (Quận 2 cũ)":"Phường Cát Lái",
        "Phường Tân Phú (Quận 9 cũ)":"Phường Tân Phú",
        "Phường Thảo Điền (Quận 2 cũ)":"Phường Thảo Điền",
        "Phường Trường Thạnh (Quận 9 cũ)":"Phường Trường Thạnh",
        "Phường Tam Phú (Quận Thủ Đức cũ)":"Phường Tam Phú",
        "Phường Trường Thạnh (Quận 9 cũ)":"Phường Trường Thạnh",
        "Phường Long Phước (Quận 9 cũ)":"Phường Long Phước",
        "Phường Bình Trưng Đông (Quận 2 cũ)":"Phường Bình Trưng Đông",
        "Phường An Khánh (Quận 2 cũ)":"Phường An Khánh",
        "Phường Bình Thọ (Quận Thủ Đức cũ)":"Phường Bình Thọ",
        "Xã Điện Thắng Trung":"Phường Điện Thắng Trung",
        # "Xã Minh Hưng":"Phường Minh Hưng",
        "Phường An Hải Tây":"Phường An Hải Nam",
        "Phường An Hải Đông":"Phường An Hải Nam",
        "Xã Long Thành":"Xã Long Thạnh",
        "Xã Tân Vĩnh Hiệp":"Phường Tân Vĩnh Hiệp",
        "Xã Hương Mạc":"Phường Hương Mạc",
        "Xã Phù Khê":"Phường Phù Khê",
        "Xã Điện Thắng Bắc":"Phường Điện Thắng Bắc",
        "Thị trấn Dương Đông":"Phường Dương Đông",
        "Phường Tam Hòa":"Phường Bình Đa",
        "Xã An Điền":"Phường An Điền",
        "Xã Phú Chánh":"Phường Phú Chánh",
        "Xã Vinh Phú":"Xã Phú Gia",
        "Xã Phong An":"Phường Phong An",
        "Xã An Tịnh":"Phường An Tịnh",
        "Xã Minh Thành":"Phường Minh Thành",
        "Xã Minh Long":"Phường Minh Long",
        "Xã Lộc Hưng":"Phường Lộc Hưng",
        "Xã Hội Nghĩa":"Phường Hội Nghĩa",
        "Xã An Nhựt Tân":"Xã Tân Bình",
        "Xã An Nhứt":"Xã Tam An",
        "Xã Tân Quới":"Thị trấn Tân Quới",
        "Xã Trường An":"Phường Trường An",
        "Xã An Ngãi":"Xã Tam An",
        "Xã Long Thuận":"Phường Long Thuận",
        "Xã Kim Long":"Thị trấn Kim Long",
        "Xã An Hòa":"Phường An Hòa",
        "Thị trấn Chơn Thành":"Phường Hưng Long",
        "Phường Trung Phụng":"Phường Khâm Thiên",
        "Xã Phú Thị":"Xã Phú Sơn",
        "Xã Đại Thành":"Xã Hưng Đạo",
        "Phường Vĩnh Trung":"Phường Thạc Gián",
        "Xã Hương An":"Thị trấn Hương An",
        "Xã Bình Hòa":"Xã Tân Bình",
        "Xã Tân Kim":"Thị trấn Cần Giuộc",
        "Xã Mỹ Phước":"Thị trấn Mỹ Phước",
        "Xã Bình Định Nam":"Xã Bình Định",
        "Thị trấn Trảng Bàng":"Phường Trảng Bàng",
        "Phường Linh Tây (Quận Thủ Đức cũ)":"Phường Linh Tây",
        "Xã Pró":"Xã Quảng Lập",
        "Xã Đại Thắng":"Xã Văn Hoàng",
        "Thị trấn Me":"Thị trấn Thịnh Vượng",
        "Xã Thư Phú":"Xã Chương Dương",
        "Xã Trường Bình":"Thị trấn Cần Giuộc",
        "Phường Tam Thuận":"Phường Xuân Hà",
        "Phường Nguyễn Trãi":"Phường Quang Trung",
        "Phường Kim Giang":"Phường Hạ Đình",
        "Thị trấn An Dương":"Phường Lê Lợi",
        "Xã Nghĩa Thắng":"Xã Phúc Thắng",
        "Xã An Hiệp":"Xã Tường Đa",
        "Phường Tân Chính":"Phường Chính Gián",
        "Xã Ea Blang":"Xã Ea Drông",
        "Thị trấn Hồ":"Phường Hồ",
        "Phường Hòa Khê":"Phường Thanh Khê Đông",
        "Xã Nghĩa Hiệp":"Xã Nguyễn Văn Linh",
        "Xã Đông Dư":"Xã Bát Tràng",
        "Phường Phước Tiến":"Phường Tân Tiến",
        "Xã Đạ Ploa":"Xã Bà Gia",
        "Xã Đạ Tồn":"Xã Đạ Oai",
        "Xã Cẩm Điền":"Xã Phúc Điền",
        "Phường Sài Đồng":"Phường Phúc Đồng",
        "Phường Hòa Thuận Đông":"Phường Bình Thuận",
        "Phường Hoá An":"Xã Long Hưng",
        "Xã Kông Pla":"Xã Kông Bơ La",
        "Xã Diên Đồng":"Xã Xuân Đồng",
        "Xã Phước Lưu":"Xã Phước Bình",
        "Xã Nghĩa An":"Xã An Phú",
        "Phường Quỳnh Lôi":"Phường Bạch Mai",
        "Xã Diên Xuân":"Xã Xuân Đồng",
        "Xã Núi Tượng":"Xã Nam Cát Tiên"
        }
    if phuong_xa in thay_the_phuong:
        phuong_xa = thay_the_phuong[phuong_xa]
        phuong_xa = unicodedata.normalize('NFD', phuong_xa).encode('ascii', 'ignore').decode('utf-8').strip().upper()
    if(ma_tinh==58):
        if(ma_quan==582):
        # "Phường Thanh Sơn":"Xã Thành Hải"
            if(phuong_xa=="Phường Thanh Sơn"):
                phuong_xa="Xã Thành Hải"
    if(ma_tinh==75):
        if(ma_quan==731):
            if(phuong_xa=="Phường Tân Tiến"):
                phuong_xa="Xã Long Hưng"
    if(ma_tinh==79):
        if(ma_quan==764):
            if(phuong_xa=="Phường 13"):
                phuong_xa="Phường 15"
            elif(phuong_xa=="Phường 9"):
                phuong_xa="Phường 8"
        if(ma_quan==765):
            if(phuong_xa=="Phường 21"):
                phuong_xa="Phường 19"
            elif(phuong_xa=="Phường 15"):
                phuong_xa="Phường 2"
    if(ma_tinh==80):
        if(ma_quan==803):
            if(phuong_xa=="Xã Tân Hòa"):
                phuong_xa="Xã Lương Hòa"
    if(ma_tinh==49):
        if(ma_quan==513):
            # "Xã Bình Chánh":"Xã Bình Phú",
            if(phuong_xa=="Xã Bình Chánh"):
                phuong_xa="Xã Bình Phú"
        if(ma_quan==509):
            if(phuong_xa=="Xã Phú Thọ"):
                phuong_xa="Xã Quế Mỹ"

    if(ma_tinh==82):
        if(ma_quan==816):
            if(phuong_xa=="Phường 3"):
                phuong_xa="Phường 2"
    if(ma_tinh==77):
        if(ma_quan==753):
            if(phuong_xa=="Xã Tam Phước"):
                phuong_xa="Xã Tam An"
            elif(phuong_xa=="Xã Lộc An"):
                phuong_xa="Xã Phước Hội"
            # "Xã Long Mỹ":"Thị trấn Phước Hải",
            elif(phuong_xa=="Xã Long Mỹ"):
                phuong_xa="Thị trấn Phước Hải"

    if(ma_tinh==1):
        if(ma_quan==275):
            if(phuong_xa=="Xã Tân Phú"):
                phuong_xa="Xã Hưng Đạo"
        if(ma_quan==18):
            if(phuong_xa=="Xã Kim Sơn"):
                phuong_xa="Xã Phú Sơn"
                # "Xã Kim Sơn":"Xã Phú Sơn",

    if(ma_tinh==31):
        if(ma_quan==312):
            if(phuong_xa=="Xã Bắc Sơn"):
                phuong_xa="Phường Tân Tiến"
    if(ma_tinh==83):
        if(ma_quan==831):
            # "Xã An Khánh":"Thị trấn Châu Thành",

            if(phuong_xa=="Xã An Khánh"):
                phuong_xa="Thị trấn Châu Thành"
    if(ma_tinh==72):
        if(ma_quan==712):
        # "Xã Bình Thạnh":"Xã Phước Bình"

            if(phuong_xa=="Xã Bình Thạnh"):
                phuong_xa="Xã Phước Bình"
    if(ma_tinh==93):
        if(phuong_xa=="Xã Đông Phú" or phuong_xa=="Thị Trấn Ngã Sáu" or phuong_xa=="Xã Đông Thạnh" or phuong_xa=="Xã Đông Phước" or phuong_xa=="Xã Phú Hữu"
           or phuong_xa=="Thị trấn Mái Dầm" or phuong_xa=="Xã Phú Tân"):
            ma_quan=933

    # Duyệt qua phường xã trong quận dựa trên mã quận
    for item in donvihanhchinh:
        if item['Mã Tỉnh'] == ma_tinh:
            for quan in item['Quận Huyện']:
                if quan['Mã Quận Huyện'] == ma_quan:
                    for phuong in quan['Cấp']:
                        if phuong_xa.strip().upper() in phuong['Tên'].strip().upper():
                            ma_phuong = phuong['Mã']
                            break  # Dừng lại khi tìm thấy phường
                        elif phuong_xa.split(" ", 1)[1].strip().upper() in phuong['Tên'].strip().upper():
                                ma_phuong = phuong['Mã']
                                break  # Dừng lại khi tìm thấy phường
                        else:
                            if phuong_xa in unicodedata.normalize('NFD', phuong['Tên']).encode('ascii', 'ignore').decode('utf-8').strip().upper():
                                ma_phuong = phuong['Mã']
                                break
                    break  # Dừng lại khi tìm thấy quận
            break  # Dừng lại khi tìm thấy tỉnh

    return ma_phuong
def so_hoa_phuong_thanh_pho_hue(phuong_xa):
    ma_phuong = 0
    ma_quan = 0  # Mã quận của thành phố Huế (Thừa Thiên Huế)
    ma_tinh=46
    # Chuẩn hóa tên phường/xã
    # if phuong_xa:
    #     phuong_xa = unicodedata.normalize('NFD', phuong_xa).encode('ascii', 'ignore').decode('utf-8').strip().upper()

    # Danh sách phường của thành phố Huế
    phuong_list_hue = [
        "Phường Thuỷ Xuân","Phường Xuân Phú","Phường Tây Lộc","Phường An Đông","Phường Phường Đúc","Phường Kim Long","Phường Hương Sơ",
        "Phường Phú Hội","Phường Vĩ Dạ","Phường Vỹ Dạ","Phường An Cựu","Phường Trường An","Phường An Tây","Phường Thuỷ Biều","Phường Thuận Hòa"
    ]
    
    # Kiểm tra xem phường có trong danh sách phường của thành phố Huế không
    if phuong_xa in phuong_list_hue:
        # Mã phường tương ứng
        phuong_map = {
            "Phường Thuỷ Xuân": 19813,
            "Phường Xuân Phú":19792,
            "Phường Tây Lộc":19750,
            "Phường An Đông":19815,
            "Phường Phường Đúc":19780,
            "Phường Kim Long":19774,
            "Phường Hương Sơ":19804,
            "Phường Phú Hội":19786,
            "Phường Vĩ Dạ":19777,
            "Phường Vỹ Dạ":19777,
            "Phường An Cựu":19801,
            "Phường Trường An":19795,
            "Phường An Tây":19816,
            "Phường Thuỷ Biều":19807,
            "Phường Thuận Hòa":19762
        }
        
        # Trả về mã phường và mã quận (Thừa Thiên Huế có mã quận là 46)
        ma_phuong = phuong_map.get(phuong_xa, 0)  # Nếu không tìm thấy, trả về 0
    for item in donvihanhchinh:
        if item['Mã Tỉnh'] == ma_tinh:
            for quan in item['Quận Huyện']:
                for phuong in quan['Cấp']:
                    if ma_phuong == phuong['Mã']:
                        ma_quan=quan["Mã Quận Huyện"]
                        break  # Dừng lại khi tìm thấy phường
            break  # Dừng lại khi tìm thấy tỉnh

    return ma_phuong, ma_quan  # Trả về cả mã phường và mã quận
def apply_so_hoa_phuong(row):
    if row['Thành Phố / Tỉnh'] == "Thừa Thiên Huế" and row['Quận / Huyện'] == "Thành phố Huế":  # Nếu chỉ có phường
        ma_phuong, ma_quan = so_hoa_phuong_thanh_pho_hue(row['Phường / Xã'])
        return pd.Series([ma_phuong, ma_quan])  # Trả về mã phường và mã quận