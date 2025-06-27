chuoi = input("Nhap mot chuoi: ")
dem_ky_tu = {}

for ky_tu in chuoi:
    if ky_tu in dem_ky_tu:
        dem_ky_tu[ky_tu] += 1
    else:
        dem_ky_tu[ky_tu] = 1

print("So lan xuat hien cua moi ky tu:")
for ky_tu, so_lan in dem_ky_tu.items():
    print(f"Ky tu '{ky_tu}': {so_lan} lan")