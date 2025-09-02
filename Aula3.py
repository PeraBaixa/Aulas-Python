"""idade = 20
altura = 1.75
ativo = True
lista = []

print(f"variável idade contém o valor {idade} e é do tipo {type(idade)}")
print(f"variável altura o valor {altura} e é do tipo {type(altura)}")
print(f"variável ativo contém o valor {ativo} e é do tipo {type(ativo)}")
print(f"variável lista contém o valor {lista} e é do tipo {type(lista)}")"""

print("Informe a operação desejada:")
print("#1: soma")
print("#2: subtração")
print("#3: multiplicação")
print("#4: divisão")
opc = input("Opção: ")
texto = "Você selecionou "
oper = ""

if opc == "1":
    oper = '+'
    texto += 'SOMA'
elif opc == "2":
    oper = '-'
    texto += 'SUBTRAÇÃO'
elif opc == "3":
    oper = '*'
    texto += 'MULTIPLICAÇÃO'
else:
    oper = '/'
    opc = "4"
    texto += 'DIVISÃO'
print(texto)

v1 = int(input("Digite o primeiro valor da operação: "))
v2 = int(input("Digite o segundo valor da operação: "))
res = 0

match opc:
    case "1":
        res = v1 + v2
    case "2":
        res = v1 - v2
    case "3":
        res = v1 * v2
    case "4":
        if v2 != 0:
            res = v1 / v2
        else:
            res = "erro"

if isinstance(res, str):
    print("Erro! Divisão por zero não existe!")
else:
    print(f"O resultado final da operação {v1} {oper} {v2} é {res}")
    print("Obrigado!")

"""notas = []
media = 0.0
qtnotas = 3
notamaior = 0.0
notamenor = 11.0

for i in range(qtnotas):
    notas.append(float(input("Nota "+ str(i+1) +" do aluno: ")))
    media += notas[i]
    if notas[i] > notamaior:
        notamaior = notas[i]
    if notas[i] < notamenor:
        notamenor = notas[i]

media /= qtnotas
print("As notas do aluno são " + str(notas))
print(f"A média das notas é {media:.2f}")
print(f"A maior nota é {notamaior} e a menor é {notamenor}")"""
