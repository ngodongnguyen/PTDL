def chuyen_chieu_ngang_sang_m(row):
    chieu_ngang = row['ChieuNgang']
    dien_tich = row['DienTichDat']  # Cột diện tích đã chuẩn hóa trước đó

    if isinstance(chieu_ngang, int):
        chieu_ngang = float(dien_tich) / 2

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
