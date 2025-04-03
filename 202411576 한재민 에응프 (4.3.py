def ohm_law_calculator():
    print("옴의 법칙 계산기")
    print("V = I × R")
    print("1. 전압(V) 계산")
    print("2. 전류(I) 계산")
    print("3. 저항(R) 계산")
    
    choice = input("계산할 값을 선택하세요 (1-3): ")
    
    if choice == "1":
        # 전압 계산
        try:
            current = float(input("전류(I)를 입력하세요 (A): "))
            resistance = float(input("저항(R)을 입력하세요 (Ω): "))
            voltage = current * resistance
            print(f"전압(V) = {voltage:.2f} V")
        except ValueError:
            print("올바른 숫자를 입력하세요.")
            
    elif choice == "2":
        # 전류 계산
        try:
            voltage = float(input("전압(V)를 입력하세요 (V): "))
            resistance = float(input("저항(R)을 입력하세요 (Ω): "))
            current = voltage / resistance
            print(f"전류(I) = {current:.2f} A")
        except ValueError:
            print("올바른 숫자를 입력하세요.")
            
    elif choice == "3":
        # 저항 계산
        try:
            voltage = float(input("전압(V)를 입력하세요 (V): "))
            current = float(input("전류(I)를 입력하세요 (A): "))
            resistance = voltage / current
            print(f"저항(R) = {resistance:.2f} Ω")
        except ValueError:
            print("올바른 숫자를 입력하세요.")
            
    else:
        print("1, 2, 3 중에서 선택하세요.")

if __name__ == "__main__":
    while True:
        ohm_law_calculator()
        again = input("\n다시 계산하시겠습니까? (y/n): ")
        if again.lower() != 'y':
            break 