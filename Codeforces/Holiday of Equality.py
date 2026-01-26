

n = int(input())
charges = list(map(int,input().split()))

spend = 0
m = max(charges)
for b in range(0,len(charges)):
    if charges[b] != m:
        spend += m-charges[b]
    else:
        spend +=0
print(spend)