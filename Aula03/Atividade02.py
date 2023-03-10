salario = 2000
nome = input("Informe o nome do vendedor: ")
mes = int(input("Informe o número do mês de venda (1 a 12): "))
#fazendo com if e else pois os alunos ainda não conhecem dict
if mes == 1:
    mes = 'janeiro'
elif mes == 2:
    mes = 'fevereiro'
elif mes == 3:
    mes = 'março'
elif mes == 4:
    mes = 'abril'
elif mes == 5:
    mes = 'maio'
elif mes == 6:
    mes = 'junho'
elif mes == 7:
    mes = 'julho'
elif mes == 8:
    mes = 'agosto'
elif mes == 9:
    mes = 'setembro'
elif mes == 10:
    mes = 'outubro'
elif mes == 11:
    mes = 'novembro'
elif mes == 12:
    mes = 'dezembro'

venda = float(input(f"Informe o valor vendido por '{nome}' no mês de {mes}: "))

if venda > 30000:
    salario = salario + (venda*0.05)
elif venda > 15000:
    salario = salario + (venda*0.04)
else:
    salario = salario + (venda*0.025)

print(f"{nome} vendeu R$ {venda:.2f} em {mes} e deve receber R$ {salario:.2f}.")


