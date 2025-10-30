import sys
m,n = map(int,sys.stdin.readline().split())
if m > 16 or n > 16 and m <1 or n<1:
    print("Numeros incorrectos")
else:
    print((m*n)//2)