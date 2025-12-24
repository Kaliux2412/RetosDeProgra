import sys

matrix = []

for n in range(5):
    m = list(map(int,sys.stdin.readline().split()))
    matrix.append(m)

for k in range(5):
    for j in range(5):
        if matrix[k][j] == 1:
            posicion = [k,j]

if posicion[1] != 2 or posicion[0] != 2:
    moves = 0
    for m in range(posicion[0],5):
        for n in range(posicion[1],5):
            if matrix[2][2] != 1:
                    while 1 not in matrix[2]:
                        if m > 2:
                            matrix[m],matrix[m-1] = matrix[m-1],matrix[m]
                            
                            moves +=1
                            m=m-1
                        else:
                            matrix[m],matrix[m+1] = matrix[m+1],matrix[m]
                            
                            moves +=1
                            m=m+1
                        
    

                    while matrix[2][2] !=1:
                        if n > 2:
                            matrix[2][n], matrix[2][n-1] = matrix[2][n-1], matrix[2][n]
                            
                            moves +=1
                            n=n-1
                        else:
                            matrix[2][n], matrix[2][n+1] = matrix[2][n+1], matrix[2][n]
                            
                            moves +=1
                            n=n+1
                    break
else:
    moves = 0

print(moves)

