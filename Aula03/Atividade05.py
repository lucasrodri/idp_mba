temp = float(input("Informe uma temperatura: "))
tipo = int(input("Esta temperatura está em Celsius ou Faherenheit (1 para Celsius, 2 para Faherenheit): "))
while tipo != 1 and tipo != 2:
    print("O tipo está errado! (1 para Celsius, 2 para Faherenheit)")
    tipo = int(input("Esta temperatura está em Celsius ou Faherenheit (1 para Celsius, 2 para Faherenheit): "))
if tipo == 1:
    tempFinal = (temp*(9/5)) + 32
    print(f"A temperatura de {temp:.2f} Celsius em Faherenheit é {tempFinal:.2f} ")
else:
    tempFinal = (temp-32)*(5/9)
    print(f"A temperatura de {temp:.2f} Faherenheit em Celsius é {tempFinal:.2f} ")

