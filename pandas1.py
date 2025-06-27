import pandas as pd

# 1. Tạo DataFrame df_students
data = {
    'Name': ['An', 'Bình', 'Cường', 'Dung', 'Hà', 'Khánh', 'Lan', 'Mai', 'Nam', 'Phong'],
    'Age': [20, 21, 19, 20, 22, 20, 21, 19, 20, 21],
    'Gender': ['M', 'F', 'M', 'F', 'F', 'M', 'F', 'F', 'M', 'M'],
    'Score': [8.5, 4.0, 7.5, 6.0, 9.0, 3.5, 8.0, 5.5, 4.5, 7.0]
}
df_students = pd.DataFrame(data)

# 2. Hiển thị toàn bộ dữ liệu
print("Toàn bộ dữ liệu:")
print(df_students)
print()

# 3. Hiển thị 3 dòng đầu tiên
print("3 dòng đầu tiên:")
print(df_students.head(3))
print()

# 4. Hiển thị theo index=2 và cột Name
print("Tên sinh viên tại index=2:")
print(df_students.loc[2, 'Name'])
print()

# 5. Hiển thị theo index=10 và cột Age
# Lưu ý: index=10 vượt quá số dòng (0-9), nên sẽ báo lỗi hoặc trả về NaN
try:
    print("Tuổi sinh viên tại index=10:")
    print(df_students.loc[10, 'Age'])
except KeyError:
    print("Index=10 không tồn tại")
print()

# 6. Hiển thị các cột Name và Score
print("Cột Name và Score:")
print(df_students[['Name', 'Score']])
print()

# 7. Thêm cột Pass dựa trên điều kiện Score >= 5
df_students['Pass'] = df_students['Score'] >= 5
print("DataFrame sau khi thêm cột Pass:")
print(df_students)
print()

# 8. Sắp xếp theo Score giảm dần
print("Danh sách sinh viên sắp xếp theo Score giảm dần:")
print(df_students.sort_values(by='Score', ascending=False))