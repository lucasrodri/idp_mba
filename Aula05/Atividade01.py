"""
Na apostila da aula 3, vimos um exercício sobre cálculo de vacinas aplicadas na região sudeste. Havia um dicionário nele:

Sem consultar a apostila, calcule:

    o total de doses aplicadas na região norte,
    a proporção desse total em relação a todo o Brasil.

"""
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

total = 0
for estado in estados:
    if estado["uf"] in ["AM", "RR", "AP", "PA", "TO", "RO", "AC"]:
        total += estado["doses"]
print(f"Total de doses aplicadas na região norte: {total}")
print(f"Proporção desse total em relação a todo o Brasil: {total / sum([estado['doses'] for estado in estados]) * 100:.2f}%")

"""
import statistics as st
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Calculando a média
media = st.mean(lista)
#Calculando a mediana
mediana = st.median(lista)
#Calculando a moda
moda = st.mode(lista)
#Calculando o desvio padrão
desvio_padrao = st.stdev(lista)
#Calculando a variância
variancia = st.variance(lista)
"""