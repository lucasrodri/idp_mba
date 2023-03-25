"""
A regra para calcular o volume de uma esfera é: V=4/3πr3, sendo r=raio. Crie uma função que retorna o volume de qualquer esfera a partir do seu raio.
"""
import math
def volume_esfera(raio):
    return 4/3 * math.pi * raio ** 3
print(f"O volume da esfera de raio 10 é {volume_esfera(10):.2f}")
print(f"O volume da esfera de raio 10 é {volume_esfera(15):.2f}")
print(f"O volume da esfera de raio 10 é {volume_esfera(18):.2f}")
print(f"O volume da esfera de raio 10 é {volume_esfera(25):.2f}")
print(f"O volume da esfera de raio 10 é {volume_esfera(32):.2f}")


