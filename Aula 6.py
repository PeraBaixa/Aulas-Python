from random import randint
"""
def criaListaAleatoria():
    r = randint(1, 10)
    lista = []
    while len(lista) != r:
        lista.append(randint(1,10))
    
    return lista

numrs = [randint(1,10) for _ in range(0, 10)]

print(numrs)
lista1 = criaListaAleatoria()
lista2 = criaListaAleatoria()
lista3 = criaListaAleatoria()

print(f"1 - {len(lista1)} elementos: {lista1}")
print(f"2 - {len(lista2)} elementos: {lista2}")
print(f"3 - {len(lista3)} elementos: {lista3}")
"""

"""n = int(input("Informe a quantidade de elementos em cada lista: "))
a = [_ for _ in range(2, n+1, 2)]
b = [_ for _ in range(3, n+1, 2)]

print(f"A lista A ficou: {a}")
print(f"A lista B ficou: {b}")
c = [(a[i]+b[i]) for i in range(len(a))]
print(f"A lista C ficou: {c}")"""

"""n = int(input("Informe o tamanho dos vetores: "))
vetor1 = [randint(1, n*n) for _ in range(n)]
vetor2 = [randint(1, n*n) for _ in range(n)]

soma = [(vetor1[i] + vetor2[i]) for i in range(n)]

print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")
print(f"Vetor Soma: {soma}")"""

"""n = int(input("Informe o tamanho do vetor: "))
vetor = [randint(1, n*n) for _ in range(n)]

print(f"Vetor: {vetor}")
print(f"Maior valor: {max(vetor)}")
print(f"Posição do maior valor: {vetor.index(max(vetor))}")"""

"""n = int(input("Informe o tamanho do vetor: "))
vetor = [randint(1, n*n) for _ in range(n)]

print(f"Vetor: {vetor}")
pesc = 0
for v in vetor:
    pesc+=(v*v)
print(f"Produto escalar: {pesc}")"""

"""n = int(input("Informe o tamanho dos vetores: "))
vetor1 = [randint(1, n*n) for _ in range(n)]
vetor2 = [randint(1, n*n) for _ in range(n)]

produtos = [(vetor1[i] * vetor2[i]) for i in range(n)]

print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")
print(f"Vetor com os produtos: {produtos}")"""

"""n = int(input("Informe o tamanho do vetor: "))
vetor = [randint(1, n*n) for _ in range(n)]
par, impar = 0,0

for e in vetor:
    if e%2 == 0:
        par+=1
    else:
        impar+=1

print(f"Vetor: {vetor}")
print(f"Quantidade de valores pares: {par}")
print(f"Quantidade de valores impares: {impar}")"""

"""n = int(input("Informe o tamanho dos vetores: "))
vetor1 = [randint(1, n*n) for _ in range(n)]
vetor2 = [randint(1, n*n) for _ in range(n)]

subt = [(vetor1[i] - vetor2[i]) for i in range(n)]

print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")
print(f"Vetor com as subtrações: {subt}")"""

LINHAS = 3
COLUNAS = 3
n = 1

m = []

for l in range(LINHAS):
    vetor = []
    for c in range(COLUNAS):
        vetor.append(n)
        n+=1
    m.append(vetor)

for l in range(LINHAS):
    for c in range(COLUNAS):
        print(m[l][c], end=" ")
    print()

print("-------------")

for l in range(LINHAS-1, -1, -1):
    for c in range(COLUNAS-1, -1, -1):
        print(m[l][c], end=" ")
    print()
