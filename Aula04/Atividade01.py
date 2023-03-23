"""
Na apostila referente à primeira aula, há um exemplo em que foi calculada a área de um círculo de 12,5 metros de raio. 
Vimos ali que a fórmula para isso é A=πr2.

Retome esta fórmula para retornar os valores calculados para cada raio da lista 12,7, 29,1, 10,5 e 14,3.
"""
import math as m
def area_circulo(raio):
    return m.pi * raio ** 2

raios = [12.7, 29.1, 10.5, 14.3]
areas = [area_circulo(raio) for raio in raios]
print("As areas são:")
for area in enumerate(areas):
    print(f"Circulo {area[0]+1}: {area[1]:.2f}")


