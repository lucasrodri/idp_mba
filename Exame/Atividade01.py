"""
A sequência de números proposta pelo matemático italiano Leonardo de Pisa, mais conhecido como sequência Fibonacci, 
possui o numeral 1 como o primeiro e o segundo termo da ordem, e os elementos seguintes são originados pela soma de seus dois antecessores, observe:

    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377...

Crie um programa que calcula a sequência até 30 termos.
"""

ant = 0
atual = 1
#for i in range(30):
#    print(i+1, atual)
#    ant, atual = atual, atual + ant

#Como não foi ensinado range, faça assim:
cont = 1
while cont <= 30:
    print(cont, atual)
    ant, atual = atual, atual + ant
    cont += 1

