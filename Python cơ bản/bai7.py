def capitalize_first_letters(chuoi):
    words = chuoi.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

chuoi = input("Nhap mot chuoi: ")
ket_qua = capitalize_first_letters(chuoi)
print(f"Chuoi sau khi chuyen ky tu dau moi tu thanh in hoa: {ket_qua}")