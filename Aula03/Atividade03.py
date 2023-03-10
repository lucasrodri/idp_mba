#Escreva um código que diz se o número digitado pelo usuário é par ou ímpar.
n = int(input("Informe um número: "))
if n % 2 == 0:
    print(f"O número {n} é par")
else:
    print(f"O número {n} é ímpar")