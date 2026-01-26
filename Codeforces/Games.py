
n = int(input())
i = n 
uniform = []
while n > 0:
    u = list(map(int,input().split()))
    uniform.append(u)
    n-=1
change = 0
big = []
for h in range(0,i):
    host = uniform[h][0]
    for u in range(0,i):
        other = uniform[u][1]
        if host == other:
            change +=1
        if h == u:
            continue
        else:
            co = [host,other]
            big.append(co)
print(change)