import sys
n,k = map(int,sys.stdin.readline().split())
p = list(map(int,sys.stdin.readline().split()))
next_round = []
for i in p:
    if i >= p[k-1] and i > 0:
        next_round.append(i)
    else:
        continue
print(len(next_round))