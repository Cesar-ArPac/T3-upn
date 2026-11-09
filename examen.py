import math
import random


def simular_montecarlo(a, b, c, d, cantidad_puntos):

    puntos_en_elipse = 0
    puntos_en_interseccion = 0

    area_elipse = math.pi * a * b

    for _ in range(cantidad_puntos):

        x = random.uniform(-a, a)
        y = random.uniform(-b, b)

        dentro_elipse = (x**2 / a**2) + (y**2 / b**2) <= 1

        dentro_hiperbola = (x**2 / c**2) - (y**2 / d**2) >= 1

        if dentro_elipse:
            puntos_en_elipse += 1

            if dentro_hiperbola:
                puntos_en_interseccion += 1

    if puntos_en_elipse > 0:
        area_interseccion = area_elipse * (
            puntos_en_interseccion / puntos_en_elipse
        )
    else:
        area_interseccion = 0

    print("\n===== RESULTADOS =====")
    print("Cantidad de puntos generados:", cantidad_puntos)
    print("Puntos dentro de la elipse:", puntos_en_elipse)
    print("Puntos en la interseccion:", puntos_en_interseccion)
    print("Area de la elipse:", round(area_elipse, 4))
    print("Area aproximada de la interseccion:", round(area_interseccion, 4))


print("===== METODO DE MONTE CARLO =====")

a = float(input("Ingrese el valor de a (elipse): "))
b = float(input("Ingrese el valor de b (elipse): "))
c = float(input("Ingrese el valor de c (hiperbola): "))
d = float(input("Ingrese el valor de d (hiperbola): "))

cantidad_puntos = int(input("Ingrese la cantidad de puntos aleatorios: "))

if a <= 0 or b <= 0 or c <= 0 or d <= 0 or cantidad_puntos <= 0:

    print("Error: todos los valores deben ser positivos.")

else:

    simular_montecarlo(a, b, c, d, cantidad_puntos)