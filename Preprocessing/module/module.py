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
    global count
    count+=1
    if(count==114):
        print(quan_huyen)
    if quan_huyen=="Thị xã Bến Cát":
        quan_huyen="Thành phố Bến Cát"
        quan_huyen = unicodedata.normalize('NFD', quan_huyen).encode('ascii', 'ignore').decode('utf-8').strip().upper()
    if quan_huyen=="Thị xã Phú Mỹ":
        quan_huyen="Thành phố Phú Mỹ"
        quan_huyen = unicodedata.normalize('NFD', quan_huyen).encode('ascii', 'ignore').decode('utf-8').strip().upper()
    if quan_huyen=="Huyện Chơn Thành":
        quan_huyen="Thị xã Chơn Thành"
        quan_huyen = unicodedata.normalize('NFD', quan_huyen).encode('ascii', 'ignore').decode('utf-8').strip().upper()

    # Duyệt qua quận huyện trong tỉnh dựa trên mã tỉnh
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

    # Duyệt qua phường xã trong quận dựa trên mã quận
    for item in donvihanhchinh:
        if item['Mã Tỉnh'] == ma_tinh:
            for quan in item['Quận Huyện']:
                if quan['Mã Quận Huyện'] == ma_quan:
                    for phuong in quan['Cấp']:
                        if phuong_xa.strip().upper() in phuong['Tên'].strip().upper():
                            ma_phuong = phuong['Mã']
                            break  # Dừng lại khi tìm thấy phường
                    break  # Dừng lại khi tìm thấy quận
            break  # Dừng lại khi tìm thấy tỉnh

    return ma_phuong