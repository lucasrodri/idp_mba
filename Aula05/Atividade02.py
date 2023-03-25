"""
Numa escola, para o aluno ser aprovado, ele precisa:

    ter 75% de presença de um total de 15 aulas
    ter nota média acima de 7.0

Os dados que temos são estes:

Com essas informações:

    Responda qual é a média de idade da turma
    Responda qual é a nota média de bolsistas
    Responda qual é a nota média de não bolsistas
    Adicione, para cada aluno, um item chamado "aprovado", com valor que pode ser True ou False

"""
alunos = [
    {"nome": "João", "idade": 25, "bolsista": True, "faltas": 2, "nota": 8.0},
    {"nome": "Maria", "idade": 23, "bolsista": False, "faltas": 0, "nota": 7.5},
    {"nome": "Ana", "idade": 22, "bolsista": False, "faltas": 3, "nota": 8.0},
    {"nome": "Pedro", "idade": 24, "bolsista": False, "faltas": 1, "nota": 5.5},
    {"nome": "Antonio", "idade": 26, "bolsista": True, "faltas": 0, "nota": 6.5},
    {"nome": "Ernesto", "idade": 22, "bolsista": False, "faltas": 4, "nota": 7.5},
    {"nome": "Joana", "idade": 21, "bolsista": True, "faltas": 1, "nota": 9.0},
    {"nome": "Enzo", "idade": 21, "bolsista": True, "faltas": 3, "nota": 6.5}
]
nfaltas = 15 - (15 * 0.75) 
media = sum([aluno["idade"] for aluno in alunos]) / len(alunos)
print(f"Média de idade da turma: {media:.2f}")
media = sum([aluno["nota"] for aluno in alunos if aluno["bolsista"]]) / len([aluno for aluno in alunos if aluno["bolsista"]])
print(f"Nota média de bolsistas: {media:.2f}")
media = sum([aluno["nota"] for aluno in alunos if not aluno["bolsista"]]) / len([aluno for aluno in alunos if not aluno["bolsista"]])
print(f"Nota média de não bolsistas: {media:.2f}")
for aluno in alunos:
    aluno["aprovado"] = aluno["faltas"] < nfaltas and aluno["nota"] >= 7.0
print("Nome\tIdade\tBolsista\tFaltas\tNota\tAprovado")
for aluno in alunos:
    bolsista = "Sim" if aluno['bolsista'] else "Não"
    aprovado = "Sim" if aluno['aprovado'] else "Não"
    print(f"{aluno['nome']}\t{aluno['idade']}\t{bolsista}\t\t{aluno['faltas']}\t{aluno['nota']}\t{aprovado}")