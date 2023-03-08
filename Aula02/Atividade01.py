#Categorias:
"""
    Menos que 0º é congelante,
    De 0º a 10º é muito frio,
    De 10,1º a 17º é friozinho,
    De 17,1º a 24º é ameno,
    De 24,1º a 30º é calor,
    Acima de 30º é muito calor.
"""
#Usuário informa a temperatura
temperatura = input("Informe a temperatura atual: ")
#Convertendo a variável para float (numero real)
temperatura = float(temperatura)
#Retornando ao usuário a informação sobre a temperatura de acordo com a tabela:
if temperatura < 0:
    print("Hoje tá congelante.")
elif temperatura <= 10:
    print("Tá um muito frio hoje!")
elif temperatura <= 17:
    print("Hoja tá fazendo um friozinho.")
elif temperatura <= 30:
    print("Tá um calor hoje!!!")
else:
    print("Hoje tá muito calor!!!")