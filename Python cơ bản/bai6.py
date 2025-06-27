def tach_ho_ten(fullname):
    parts = fullname.strip().split()
    
    if not parts:
        return "", ""
    ten = parts[-1]
    ho_lot = " ".join(parts[:-1]) if len(parts) > 1 else ""
    return ho_lot, ten

ho_ten = input("Nhap ho ten: ")
ho_lot, ten = tach_ho_ten(ho_ten)

print(f"Ho lot: {ho_lot}")
print(f"Ten: {ten}")