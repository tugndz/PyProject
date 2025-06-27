import time

def generate_random_number():
    ms = int(time.time() * 1000) % 1000
    return (ms % 999) + 1 

def guess_number_game():
    target = generate_random_number()
    wrong_guesses = 0
    
    while True:
        try:
            guess = int(input("Nhap mot so nguyen duong tu 1 den 999: "))
            
            if guess < 1 or guess > 999:
                print("Vui long nhap so trong khoang tu 1 den 999.")
                continue
            
            if guess == target:
                print(f"Ban da du doan chinh xac so {target}")
                break
            
            wrong_guesses += 1
            
            if abs(guess - target) <= 10:
                print("Ban doan gan dung roi!")
            
            if wrong_guesses >= 5:
                print("Ban doan trat tat ca nam lan, ket qua da thay doi. Moi ban doan lai")
                target = generate_random_number()
                wrong_guesses = 0
            else:
                print(f"Ban da tra loi sai {wrong_guesses} lan")
                
        except ValueError:
            print("Vui long nhap mot so nguyen hop le.")
            continue

print("Chao mung den voi tro choi Doan so!")
guess_number_game()