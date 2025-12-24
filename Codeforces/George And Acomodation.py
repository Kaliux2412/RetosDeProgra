import sys


n = int(sys.stdin.readline())
a = []
while n > 0:
    p,q = map(int,sys.stdin.readline().split())
    v = [p,q]
    a.append(v)
    n -= 1
possible_rooms = 0
for i in range(0,len(a)):
    if a[i][0] <= (a[i][1])-2:
        possible_rooms +=1
print(possible_rooms)