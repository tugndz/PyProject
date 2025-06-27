import pandas as pd
import numpy as np

# Tạo bảng Nhân viên
du_lieu_nhan_vien = {
    'ID': [101, 102, 103, 104, 105, 106],
    'Ten': ['An', 'Bình', 'Cường', 'Dương', np.nan, 'Hạnh'],
    'Tuoi': [25, np.nan, 30, 22, 28, 35],
    'Phong_ban': ['HR', 'IT', 'IT', 'Finance', 'HR', np.nan],
    'Luong': [700, 800, 750, np.nan, 710, 770]
}
bang_nv = pd.DataFrame(du_lieu_nhan_vien)

# Tạo bảng Phòng ban
du_lieu_phong_ban = {
    'Phong_ban': ['HR', 'IT', 'Finance', 'Marketing'],
    'Quan_ly': ['Trang', 'Khoa', 'Minh', 'Lan']
}
bang_pb = pd.DataFrame(du_lieu_phong_ban)

# Kiểm tra giá trị thiếu
print("Thiếu dữ liệu:\n", bang_nv.isnull().sum())

# Xoá dòng có hơn 2 giá trị bị thiếu
bang_nv = bang_nv[bang_nv.isnull().sum(axis=1) <= 2]

# Điền giá trị thiếu
bang_nv['Ten'].fillna('Chưa rõ', inplace=True)
tuoi_tb = round(bang_nv['Tuoi'].mean())
bang_nv['Tuoi'].fillna(tuoi_tb, inplace=True)
bang_nv['Phong_ban'].fillna('Unknown', inplace=True)
bang_nv['Luong'].fillna(method='ffill', inplace=True)

# Đổi kiểu dữ liệu
bang_nv['Tuoi'] = bang_nv['Tuoi'].astype(int)
bang_nv['Luong'] = bang_nv['Luong'].astype(int)

# Tạo cột Lương sau thuế
bang_nv['Luong_sau_thue'] = (bang_nv['Luong'] * 0.9).astype(int)

# Lọc nhân viên IT và tuổi > 25
nv_it_tren_25 = bang_nv[(bang_nv['Phong_ban'] == 'IT') & (bang_nv['Tuoi'] > 25)]

# Sắp xếp theo lương sau thuế giảm dần
bang_nv = bang_nv.sort_values(by='Luong_sau_thue', ascending=False)

# Tính lương trung bình theo phòng ban
luong_tb_phong_ban = bang_nv.groupby('Phong_ban')['Luong'].mean().reset_index()

# Nối với bảng Phòng ban để biết quản lý
bang_nv_day_du = pd.merge(bang_nv, bang_pb, on='Phong_ban', how='left')

# Thêm 2 nhân viên mới
nhan_vien_moi = pd.DataFrame({
    'ID': [107, 108],
    'Ten': ['Khôi', 'Linh'],
    'Tuoi': [26, 29],
    'Phong_ban': ['Marketing', 'Finance'],
    'Luong': [780, 820]
})
nhan_vien_moi['Luong_sau_thue'] = (nhan_vien_moi['Luong'] * 0.9).astype(int)

# Gộp vào bảng chính
bang_nv_day_du = pd.concat([bang_nv_day_du, nhan_vien_moi], ignore_index=True)

# Xuất kết quả
print("\nBảng nhân viên hoàn chỉnh:")
print(bang_nv_day_du)

print("\nNhân viên IT trên 25 tuổi:")
print(nv_it_tren_25)

print("\nLương trung bình theo phòng ban:")
print(luong_tb_phong_ban)