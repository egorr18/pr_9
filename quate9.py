print("Таємниці Всесвіту!")

while True:
    print("\nОбери розрахунок:")
    print("1 - Космічна відстань")
    print("2 - Спрощена гравітація")
    print("3 - Наближення сповільнення часу")
    choice = input("Введи номер опції (1/2/3): ")

    try:
        if choice == "1":
            v = float(input("Частка швидкості світла (0-1): "))
            t = float(input("Час у роках: "))
            result = v * t
            print(f"Космічна відстань: {result:.4f} світлових років")

        elif choice == "2":
            m1 = float(input("Маса 1: "))
            m2 = float(input("Маса 2: "))
            factor_input = input("Космічний множник (Enter для 1.0): ")
            factor = float(factor_input) if factor_input else 1.0
            result = m1 * m2 * factor
            print(f"Гравітаційна взаємодія: {result:.4f}")

        elif choice == "3":
            v = float(input("Частка швидкості світла (менше 1): "))
            if v >= 1:
                print("Частка швидкості світла має бути меншою за 1.")
                continue
            t = float(input("Час у секундах: "))
            result = t / (1 - v)
            print(f"Сповільнений час: {result:.4f} секунд")

        else:
            print("Невірний вибір. Спробуй ще раз.")
            continue

    except ValueError:
        print("Помилка введення! Введи числові значення.")
        continue

    again = input("\nЩе один розрахунок? (так/ні): ").strip().lower()
    if again not in ["так", "y", "yes", "т"]:
        print("\nДякуємо за використання калькулятора 'Таємниці Всесвіту'!")
        break
