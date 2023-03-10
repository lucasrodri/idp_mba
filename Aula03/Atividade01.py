"""
#Este é um programa para calcular o fatorial de um número
numero = int(input("Digite um número de 1 a 20: "))
resultado = 1

while numero != 0: # os : aqui!
#Não está indentado
resultado = resultado * 'numero' # numero está como string
numero = numero - 1

print('O fatorial é {}.".format('resultado') # aqui tem várias coisas erradas! parenteses. Uso da função format. resultado como str. 
"""
#Codigo corrigido:
# Este é um programa para calcular o fatorial de um número
numero = int(input("Digite um número de 1 a 20: "))
resultado = 1

while numero != 0:
    resultado = resultado * numero
    numero = numero - 1

print('O fatorial é {}'.format(resultado))

