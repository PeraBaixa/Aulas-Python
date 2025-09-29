"""while True:
    A = input("Informe o valor 'A': ")
    if A.isdigit():
        A = int(A)
        if A > 0: break
    print("Valor inválido para 'A'!\n")

while True:
    B = input("Informe o valor 'B': ")
    if B.isdigit():
        B = int(B)
        if B > A: break
    print("Valor inválido para 'B'!\n")

pares = [par for par in range(A, B+1) if par%2==0]

print(pares)"""

"""v = []

while len(v) < 3:
    val = input(f"Informe o {len(v)+1}º: ")
    if val.isdigit():
        val = int(val)
        if val > 0:
            v.append(val)
        else:
            print("Valor inserido é inválido!")
    else:
        print("Valor inserido é inválido!")

print(f"O maior valor informado: {max(v)}")
print(f"O menor valor informado: {min(v)}")
print(f"A média entre todos os valores: {(v[0]+v[1]+v[2])//3}")"""

"""while True:
    v = input("Informe o valor escolhido: ")
    if v.isdigit():
        v = int(v)
        if v > 0: break
    print("Valor inválido!")

[print(f"{v}*{m} = {v*m}") for m in range(1, 11)]"""

"""while True:
    idade = input("Informe a idade da pessoa: ")
    if idade.isdigit():
        idade = int(idade)
        if idade > -1: break
    print("Valor inválido!")

if idade < 12:
    print("criança")
elif idade >= 12 and idade < 18:
    print("adolescente")
elif idade >= 18 and idade < 60:
    print("adulto")
else:
    print("idoso")"""

"""nomes = [input(f"Digite o nome {n}: ") for n in range(1,6)]

print(f"\nA lista de nomes: {nomes}")
print(f"O primeiro nome da lista: {nomes[0]}")
print(f"O último nome da lista: {nomes[4]}")"""
