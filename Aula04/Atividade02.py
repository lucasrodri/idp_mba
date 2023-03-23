"""
Na aula retrasada, fizemos uma atividade em sala que pedia ao usuário a informação de temperatura e retornava uma descrição mais ou menos assim:

    Menos que 0° é congelante,
    De 0º a 10° é muito frio,
    Acima de 10° a 17° é friozinho,
    Acima de 17° a 24° é ameno,
    Acima de 24° a 30° é calor,
    Acima de 30° é muito calor.

Esta atividade é parecida, mas em vez de uma temperatura qualquer, peça ao usuário as temperaturas de São Paulo, Rio de Janeiro, Belo Horizonte, Brasília e Recife. Adicione cada temperatura numa lista e, ao fim, retorne uma frase com a descrição de cada temperatura.

Dica: para saber a qual capital pertence cada temperatura, use a posição do valor na lista, o índice.
"""
temperaturas = []
cidades = []

cidade = "São Paulo"
cidades.append(cidade)
temperatura = float(input(f"Digite a temperatura de {cidade}: "))
temperaturas.append(temperatura)

cidade = "Rio de Janeiro"
cidades.append(cidade)
temperatura = float(input(f"Digite a temperatura de {cidade}: "))
temperaturas.append(temperatura)

cidade = "Belo Horizonte"
cidades.append(cidade)
temperatura = float(input(f"Digite a temperatura de {cidade}: "))
temperaturas.append(temperatura)

cidade = "Brasília"
cidades.append(cidade)
temperatura = float(input(f"Digite a temperatura de {cidade}: "))
temperaturas.append(temperatura)

cidade = "Recife"
cidades.append(cidade)
temperatura = float(input(f"Digite a temperatura de {cidade}: "))
temperaturas.append(temperatura)

for indice, temperatura in enumerate(temperaturas):
    if temperatura < 0:
        print(f"Em {cidades[indice]} a temperatura de {temperatura}ºC é congelante.")
    elif temperatura <= 10:
        print(f"Em {cidades[indice]} a temperatura de {temperatura}ºC é muito frio.")
    elif temperatura <= 17:
        print(f"Em {cidades[indice]} a temperatura de {temperatura}ºC é friozinho.")
    elif temperatura <= 24:
        print(f"Em {cidades[indice]} a temperatura de {temperatura}ºC é ameno.")
    elif temperatura <= 30:
        print(f"Em {cidades[indice]} a temperatura de {temperatura}ºC é calor.")
    else:
        print(f"Em {cidades[indice]} a temperatura de {temperatura}ºC é muito calor.")


