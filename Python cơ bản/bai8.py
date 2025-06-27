def alternate_case(chuoi):
    ket_qua = ""
    for i in range(len(chuoi)):
        if i % 2 == 0:
            ket_qua += chuoi[i].lower()
        else:
            ket_qua += chuoi[i].upper()
    return ket_qua
chuoi = input("Nhap mot chuoi: ")
ket_qua = alternate_case(chuoi)
print(f"Chuoi sau khi doi xen ke: {ket_qua}")