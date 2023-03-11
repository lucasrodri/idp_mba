#Exemplo do uso de format:
#numero = 3.1415
#print("O número é {:.2f}".format(numero))

#Exemplo usando f-strings:
#numero = 3.1415
#print(f"O número é {numero:.2f}")

#Letra a
#Número de pobres em 2019 e ago.2020
pobres2019 = 65229668
pobres_ago2020 = 50176044
queda = pobres2019 - pobres_ago2020
queda_percentual = (pobres2019 - pobres_ago2020) / pobres2019 * 100
print(f"O número de pobres no Brasil caiu {queda/(1*(10**6)):.2f} milhoes entre 2019 e agosto de 2020.")
print(f"Isso representa uma queda percentual de {queda_percentual:.2f}% entre 2019 e agosto de 2020.")

print("\n")

###Fazendo a diferença percentual:

total2019 = 65229668 + 61909343 + 50078060 + 21519066 + 11410989
pobres2019p = (pobres2019 * 100) / total2019
print(f"Pobres percentual {pobres2019p:.2f}%")

total_ago2020 = 50176044 + 76590769 + 56859091 + 19185258 + 8930353
pobres_ago2020p = (pobres_ago2020 * 100) / total_ago2020
print(f"Pobres percentual agosto de 2020 {pobres_ago2020p:.2f}%")

quedap = pobres2019p - pobres_ago2020p
print(f"A queda percentual foi: {quedap:.2f}%")

#Letra b
"""
2019
 	2 a menos de 4 sm 	21.519.066
	4 sm ou mais 	11.410.989
ago.2020
    2 a menos de 4 sm 	19.185.258
	4 sm ou mais 	8.930.353
"""
ricos2019 = 21519066 + 11410989
ricos_ago2020 = 19185258 + 8930353
queda = ricos2019 - ricos_ago2020
queda_percentual = (ricos2019 - ricos_ago2020) / ricos2019 * 100
print(f"O número de ricos no Brasil caiu {queda/(1*(10**6)):.2f} milhoes entre 2019 e agosto de 2020.")
print(f"Isso representa uma queda percentual de {queda_percentual:.2f}% entre 2019 e agosto de 2020.")


###Fazendo a diferença percentual:

total2019 = 65229668 + 61909343 + 50078060 + 21519066 + 11410989
ricos2019p = (ricos2019 * 100) / total2019
print(f"Ricos percentual {ricos2019p:.2f}%")

total_ago2020 = 50176044 + 76590769 + 56859091 + 19185258 + 8930353
ricos_ago2020p = (ricos_ago2020 * 100) / total_ago2020
print(f"Ricos percentual agosto de 2020 {ricos_ago2020p:.2f}%")

quedap = ricos2019p - ricos_ago2020p
print(f"A queda percentual foi: {quedap:.2f}%")