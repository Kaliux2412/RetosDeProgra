import random
from os import system

tablero = [
    ["O", "O", "X"],
    ["X", "X", "O"],
    ["O", "O", "X"],
]
def puntaje(fichas):
        ganador = False
        for f in range(0,3):
            ficha_inicial = tablero[0][f]
            if ficha_inicial != "" and (all(x == fichas[f][0] for x in fichas[f])):
                print(f"Gano {fichas[f][0]}")

            elif ficha_inicial != " " and all(tablero[fila][f] == ficha_inicial for fila in range(3)):
                print(f"Gano {ficha_inicial}")
                ganador = True
            elif all(tablero[f][f] == ficha_inicial for f in range(3)):
                print(f"Gano {ficha_inicial}")
                ganador = True

        if ganador == True:
            print("Buen Juego")
        else:
            print("Empate") 
puntaje(tablero)
def hacer_tablero(ficha, ficha_elegida):
    def ficha_aleatoria(ficha):
        rand = tablero[random.randint(0,2)][random.randint(0,2)]
        if rand == " ":
             rand = ficha
        else:
             rand = ficha
        print(f"{tablero[0]}\n{tablero[1]}\n{tablero[2]}\n")
    eleccion = input("Escoje la fila y columna donde quieres poner tu ficha, escribela como: 1,1, primero fila y luego columna\n NOTA: las columnas y filas empiezan en 0 no en 1: \n  ")
    def poner_ficha(eleccion,ficha_elegida):
        instrucciones = []
        for e in eleccion:
            if e != ",":
                instrucciones.append(int(e))
        if tablero[instrucciones[0]][instrucciones[1]] != " ":
            print("Ese espacio ya esta ocupado")
        else:
            tablero[instrucciones[0]][instrucciones[1]] = ficha_elegida

        print(f"{tablero[0]}\n{tablero[1]}\n{tablero[2]}\n")

        
    while puntaje(tablero) != True:
        ficha_aleatoria(ficha)
        poner_ficha(eleccion,ficha_elegida)


ficha_ele = input("Que quieres ser 'O' o 'X'")
for x in range(0,6):
    if ficha_ele == "O":
        print("De acuerdo seras circulo y yo X, inicio yo")
        hacer_tablero("X",ficha_ele)
        system("cls")
        print(f"{tablero[0]}\n{tablero[1]}\n{tablero[2]}\n")
        

    elif ficha_ele == "X":
                print("De acuerdo seras las X y yo los circulos O, inicio yo")
                hacer_tablero("O",ficha_ele)
                system("cls")
                print(f"{tablero[0]}\n{tablero[1]}\n{tablero[2]}\n")
                

