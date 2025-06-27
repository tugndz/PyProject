def is_palindrome(chuoi):
    chuoi = ''.join(char.lower() for char in chuoi if char.isalnum())
    return chuoi == chuoi[::-1]

chuoi = input("Nhap mot chuoi: ")
if is_palindrome(chuoi):
    print(f"Chuoi '{chuoi}' la chuoi doi xung.")
else:
    print(f"Chuoi '{chuoi}' khong phai la chuoi doi xung.")