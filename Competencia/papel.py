import sys

def papel():
    datos = sys.stdin.read().splitlines()
    n, k = map(int, datos[0].split())
    patron = []
    for i in range(1, 1 + n):
        patron.append(datos[i].strip())
    tama = n**k
    base = [['.' for _ in range(tama)] for _ in range(tama)]
    
    def llenar(x, y, nivel):
        if nivel == 0:
            for i in range(n):
                for j in range(n):
                    base[x + i][y + j] = patron[i][j]
            return
        sig = n ** (nivel - 1)
        for i in range(n):
            for j in range(n):
                if patron[i][j] == '#':
                    llenar(x + i * sig, y + j * sig, nivel - 1)
    
    llenar(0, 0, k - 1)
    
    for row in base:
        print(''.join(row))

papel()