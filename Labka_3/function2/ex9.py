def sphere_volume(radius):
    import math
    return (4 / 3) * math.pi * radius ** 3

# Использование
radius = float(input("Введите радиус сферы: "))
print(f"Объём сферы с радиусом {radius} равен {sphere_volume(radius):.2f}")
