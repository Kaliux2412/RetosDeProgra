import sys
n = int(sys.stdin.readline())
lista =[]
for _ in range(n):
    s,e = map(int,sys.stdin.readline().split())
    par = [s,e]
    lista.append(par)

valores = []
pasajeros =(lista[0][1] - lista[0][0])
for num in range(1,n-1):
    pasajeros = pasajeros + lista[num][1] - lista[num][0]
    valores.append(pasajeros)
mini = max(valores)

print(mini)