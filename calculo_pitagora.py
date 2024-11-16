'''
Crear un programa que permita solucionar un problema a través del
teorema de Pitágoras. Calcular la Hipotenusa a partir de los catetos
ingresados por le usario
'''
import math as m
a = float(input('Ingresa el cateto a: '))
b = float(input('Ingresa el cateto b: '))
hip = m.sqrt(a**2+b**2)
print(f'El valor de la Hipotenussa es: {round(hip, 3)}')