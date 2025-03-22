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

