def number_to_words(num):
    units = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tens = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", 
            "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    
    if not (100 <= num <= 999):
        return "Vui long nhap so co 3 chu so."
    
    tram = num // 100
    chuc = (num % 100) // 10
    don_vi = num % 10  
    result = units[tram] + " trăm"
    
    if chuc > 0:
        result += " " + tens[chuc]
    elif don_vi > 0:
        result += " lẻ"
    
    if don_vi > 0:
     
        if don_vi == 1 and chuc > 1:
            result += " mốt"
  
        elif don_vi == 5 and chuc > 0:
            result += " lăm"
        else:
            result += " " + units[don_vi]
    
    return result.strip()

try:
    num = int(input("Nhap mot so co 3 chu so: "))
    ket_qua = number_to_words(num)
    print(f"So {num} doc la: {ket_qua}")
except ValueError:
    print("Vui long nhap mot so nguyen hop le.")