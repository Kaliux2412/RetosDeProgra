import sys
n,m,a = map(int,sys.stdin.readline().split())
print(m)
cuadro_n = (n+a-1)//a
cuadro_m = (m+a-1)//a
print(cuadro_n*cuadro_m)