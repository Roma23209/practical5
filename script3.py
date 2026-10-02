import math
def calculate_rectangle_area(width, height):
    return width * height
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)
def main():
    print("--- Расчет площади прямоугольника ---")
    try:
        rect_width = float(input("Введите ширину прямоугольника: "))
        rect_height = float(input("Введите высоту прямоугольника: "))

        if rect_width <= 0 or rect_height <= 0:
            print("Ошибка: стороны прямоугольника должны быть больше нуля.")
        else:
            rect_area = calculate_rectangle_area(rect_width, rect_height)
            print(f"Площадь прямоугольника: {rect_area:.2f}")

    except ValueError:
        print("Ошибка: введено некорректное число.")

    print("\n--- Расчет площади круга ---")
    try:
        circle_radius = float(input("Введите радиус круга: "))

        if circle_radius <= 0:
            print("Ошибка: радиус круга должен быть больше нуля.")
        else:
            circle_area = calculate_circle_area(circle_radius)
            print(f"Площадь круга: {circle_area:.2f}")

    except ValueError:
        print("Ошибка: введено некорректное число.")
if __name__ == "__main__":
    main()
