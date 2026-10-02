import math
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
def calculate_triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area
def main():
    print("--- Расчет площади треугольника по координатам вершин ---")
    try:
        x_a = float(input("Введите x для точки A: "))
        y_a = float(input("Введите y для точки A: "))
        x_b = float(input("Введите x для точки B: "))
        y_b = float(input("Введите y для точки B: "))
        x_c = float(input("Введите x для точки C: "))
        y_c = float(input("Введите y для точки C: "))
        side_ab = calculate_distance(x_a, y_a, x_b, y_b)
        side_bc = calculate_distance(x_b, y_b, x_c, y_c)
        side_ca = calculate_distance(x_c, y_c, x_a, y_a)
        if (side_ab + side_bc <= side_ca) or (side_ab + side_ca <= side_bc) or (side_bc + side_ca <= side_ab):
            print("Ошибка: Треугольник с такими координатами не существует (точки лежат на одной прямой).")
            return
        triangle_area = calculate_triangle_area(side_ab, side_bc, side_ca)
        print(f"\nДлины сторон: AB = {side_ab:.2f}, BC = {side_bc:.2f}, CA = {side_ca:.2f}")
        print(f"Площадь треугольника: {triangle_area:.2f}")
    except ValueError:
        print("Ошибка: введены некорректные числовые значения.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
if __name__ == "__main__":
    main()
