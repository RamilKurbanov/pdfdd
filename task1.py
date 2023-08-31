def check_triangle_existence(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def classify_triangle(a, b, c):
    if a == b == c:
        return "Равносторонний треугольник"
    elif a == b or a == c or b == c:
        return "Равнобедренный треугольник"
    else:
        return "Разносторонний треугольник"

a = float(input("Введите длину первой стороны a: "))
b = float(input("Введите длину второй стороны b: "))
c = float(input("Введите длину третьей стороны c: "))

if check_triangle_existence(a, b, c):
    triangle_type = classify_triangle(a, b, c)
    print("Треугольник существует и он является", triangle_type)
else:
    print("Треугольник с такими сторонами не существует.")