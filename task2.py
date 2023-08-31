def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

while True:
    try:
        number = int(input("Введите число (от 2 до 100000): "))
        if number < 2 or number > 100000:
            print("Число должно быть от 2 до 100000. Попробуйте снова.")
        else:
            break
    except ValueError:
        print("Некорректный ввод. Попробуйте снова.")

if is_prime(number):
    print(f"{number} - простое число.")
else:
    print(f"{number} - составное число.")