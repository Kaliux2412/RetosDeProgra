import sys
n = int(sys.stdin.readline())
solutions = []
solve = 0
for num in range(0,n):
    p,v,t = map(int,sys.stdin.readline().split())
    orden = [p,v,t]
    solutions.append(orden)
for s,fila in enumerate(solutions):
    si = fila.count(1)
    if si >=2:
        solve +=1
print(solve)
