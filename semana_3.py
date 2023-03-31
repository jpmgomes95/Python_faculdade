NumNotas = 0
notas = []
media = 0.0

nome = input("Qual o nome do aluno? ")
NumNotas = int(input("Qual o numero de notas ? "))


for contador in range (0,NumNotas):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)

for contador in range (0, NumNotas):
    media = media + nota

media = media/NumNotas

print("%s teve média de %.2f" % (nome, media))