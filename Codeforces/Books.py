import sys

# def books(n,t,a):
#     a.sort()
#     tiempo = 0
#     s = 0
#     while tiempo < t:
#         tiempo+= a[s]
#         if tiempo < t:
#             s+=1
#         else:
#             break

#     print(s)
n,t = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

max_books = 0
suma =0
izq = 0

for der in range(n):
    suma += a[der]

    while suma > t:
        suma -= a[izq]
        izq += 1
    max_books = max(max_books, der - izq+1)
print(max_books)