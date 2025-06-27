def kiem_tra_va_tach_so(chuoi):
    co_so = any(char.isdigit() for char in chuoi)
    
    if not co_so:
        return False, []
    
    mang_so = [char for char in chuoi if char.isdigit()]
    return True, mang_so

chuoi = input("Nhap mot chuoi: ")
co_so, ket_qua = kiem_tra_va_tach_so(chuoi)

if co_so:
    print(f"Chuoi co chua so. Cac so la: {ket_qua}")
else:
    print("Chuoi khong chua so.")