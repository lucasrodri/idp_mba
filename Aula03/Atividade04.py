# Este bloco é a coleção de dados de todos os estados
estados = [
    {"uf": "AC", "doses": 364906},
    {"uf": "AL", "doses": 1421213},
    {"uf": "AM", "doses": 1773255},
    {"uf": "AP", "doses": 271691},
    {"uf": "BA", "doses": 6152177},
    {"uf": "CE", "doses": 3270535},
    {"uf": "DF", "doses": 1283699},
    {"uf": "ES", "doses": 2219656},
    {"uf": "GO", "doses": 3111799},
    {"uf": "MA", "doses": 3106822},
    {"uf": "MG", "doses": 9357072},
    {"uf": "MS", "doses": 1615951},
    {"uf": "MT", "doses": 1351618},
    {"uf": "PA", "doses": 2890438},
    {"uf": "PB", "doses": 1834443},
    {"uf": "PE", "doses": 3750035},
    {"uf": "PI", "doses": 1391719},
    {"uf": "PR", "doses": 5830476},
    {"uf": "RJ", "doses": 8084518},
    {"uf": "RN", "doses": 1652963},
    {"uf": "RO", "doses": 688403},
    {"uf": "RR", "doses": 222025},
    {"uf": "RS", "doses": 6832516},
    {"uf": "SC", "doses": 3225600},
    {"uf": "SE", "doses": 923887},
    {"uf": "SP", "doses": 23887012},
    {"uf": "TO", "doses": 621308}
]

# Esta linha é uma lista dos estados da região sudeste
sudeste = ["SP", "RJ", "MG", "ES"]

# Este bloco conta as vacinas de todos os estados
total = 0 # Começamos com zero em "total"...
for i in estados: # ...e para cada elemento na lista "estados"...
    total += i["doses"] #...adicionamos o valor de "doses" ao "total"

# Este bloco conta as vacinas dos estados do sudeste
vacinas_sudeste = 0 # Começamos com zero em "vacinas_sudeste"...
for i in estados: # ...e para cada elemento na lista "estados"...
    if i["uf"] in sudeste: #...se o valor de "uf" estiver na lista "sudeste"...
        vacinas_sudeste += i["doses"] #...adicionamos o valor de "doses" a "vacinas_sudeste"

# Esta linha calcula a proporção de vacinas no sudeste em relação ao total
calculo = (vacinas_sudeste / total) * 100

# Esta linha imprime o resultado
print("A região sudeste aplicou {}% do total de {} doses consumidas no Brasil".format(calculo, total))

