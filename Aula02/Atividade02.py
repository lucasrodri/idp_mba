#Pedindo ao usuário um número acima de entre 40 e 60 (dica: use input),
numero = int(input("Informe um número entre 40 e 60: "))

#validação do número:
while numero < 40 or numero > 60:
    print(f"O número {numero} não está no intervalo entre 40 e 60\n")
    numero = int(input("Informe um número entre 40 e 60: "))

#informando o número digitado:
print(f"\nO número digitado foi: {numero}")

#contando com 'pim'
print(f'Contando de 0 até {numero} com "pim" no lugar de 4 e seus múltiplos:\n')
n = 1
s = ""
while n <= numero:
    if n % 4 == 0:
        #print("pim", end=", ")
        s += "pim, "
    else:
        #print(n, end=", ")
        s += str(n) + ", "
    n += 1
print(s[:-2]+".")

