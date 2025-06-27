import math

def is_perfect_square(n):
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n

def find_numbers(a, b):
    if a >= b:
        return "Lỗi: a phải nhỏ hơn b"
    
    result = [num for num in range(a, b + 1) if num % 3 == 0 and not is_perfect_square(num)]
    
    return ", ".join(map(str, result)) if result else "Không có số nào thỏa mãn"

try:
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    
    ket_qua = find_numbers(a, b)
    print(f"Các số thỏa mãn: {ket_qua}")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")