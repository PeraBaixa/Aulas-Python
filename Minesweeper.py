from random import randint

BOMBAS = 3
LINHAS = 4
COLUNAS = 3

bombMarca = 9
grade = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]
prog = [['-' for _ in range(COLUNAS)] for _ in range(LINHAS)]
bombLocs = set()
alfabeto = "ABCDEFGHIJKLPMNOPQRSTUVWXYZ"

def criaBombas():
    bombs = set()
    while len(bombs) < BOMBAS:
        bombs.add((randint(0,LINHAS-1), randint(0,COLUNAS-1)))
    
    return bombs

def criaVisu(tela):
    print("  ", end="")
    [print(alfabeto[a], end=" ") for a in range(COLUNAS)]
    for l in range(LINHAS):
        print(f"\n{l+1}", end="|")
        for c in range(COLUNAS):
            print(tela[l][c], end="|")

def recebeValor(cod):
    coords = []
    if cod.isalpha or cod.isdigit:
        return "erro"

    if len(cod) == 2:
        if cod[0].isalpha:
            

    pass

bombLocs = criaBombas()

#[grade[b[0]][b[1]] = -1 for b in criaBombas()]
for b in bombLocs:
    grade[b[0]][b[1]] = bombMarca



#criaVisu(grade)

