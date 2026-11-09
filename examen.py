#Cesar Arredondo (n00416238)

import random
import math

print("===== METODO DE MONTE CARLO =====")

a = float(input("Ingrese el valor de a (elipse): "))
b = float(input("Ingrese el valor de b (elipse): "))

c = float(input("Ingrese el valor de c (hiperbola): "))
d = float(input("Ingrese el valor de d (hiperbola): "))

cantidad = int(input("Ingrese la cantidad de puntos aleatorios: "))

if a <= 0 or b <= 0 or c <= 0 or d <= 0 or cantidad <= 0:
    print("Error: todos los valores deben ser positivos.")

else:
    puntos_elipse = 0
    puntos_interseccion = 0

    for i in range(cantidad):

        x = random.uniform(-a, a)
        y = random.uniform(-b, b)

        elipse = (x ** 2 / a ** 2) + (y ** 2 / b ** 2) <= 1

        if elipse:
            puntos_elipse += 1

            hiperbola = (x ** 2 / c ** 2) - (y ** 2 / d ** 2) >= 1

            if hiperbola:
                puntos_interseccion += 1

    area_elipse = math.pi * a * b

    if puntos_elipse > 0:
        proporcion = puntos_interseccion / puntos_elipse
        area_interseccion = proporcion * area_elipse
    else:
        proporcion = 0
        area_interseccion = 0

    print("\n===== RESULTADOS =====")

    print("Cantidad de puntos generados:", cantidad)
    print("Puntos dentro de la elipse:", puntos_elipse)
    print("Puntos en la interseccion:", puntos_interseccion)
    print("Area de la elipse:", round(area_elipse, 4))
    print("Proporcion de interseccion:", round(proporcion, 4))
    print("Area aproximada de interseccion:", round(area_interseccion, 4))