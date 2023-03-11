#Letra a

#População de 212 milhoes de brasileiros
populacao_brasileira = 212*(10**6)
#Não elegíveis (menores de 18 anos) -> 21%
#Elegíveis = 100% - 21% = 79%

#regra de 3:
#populacao_brasileira -> 100
#elegiveis -> 79
#elegiveis = (populacao_brasileira*79)/100

elegiveis = 0.79 * populacao_brasileira
print(f"Havia cerca de {elegiveis/(1*(10**6)):.2f} milhões de brasileiros elegíveis para a vacinação em 9 de julho de 2021.")


print("\n")

#Letra b
"""
Podemos calcular o tempo necessário para vacinar toda a população elegível dividindo o número de pessoas que precisam ser vacinadas 
pelo número de pessoas que são vacinadas por dia.
"""
#Doses aplicadas depois do dia 9 de julho de 2021
doses_aplicadas_total = 82908617 + 994468
#Doses aplicadas por dia (de acordo com o dia 9 de julho de 2021)
doses_aplicadas_dia = 994468
#dias necessários:
dias = (elegiveis - doses_aplicadas_total) / doses_aplicadas_dia
print(f"São necessários {dias:.0f} dias para que toda a população elegível tenha recebido a primeira dose após o dia 9 de julho de 2021.")