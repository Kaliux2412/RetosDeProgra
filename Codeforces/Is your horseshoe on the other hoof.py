import sys


c1,c2,c3,c4 = (map(int, sys.stdin.readline().split()))
colors = [c1,c2,c3,c4]

min_needed = 0
rep = []
for n in range(0,len(colors)):
    if colors[n] not in rep:
        a = colors.count(colors[n])
        if a > 1:
            min_needed += a-1
            rep.append(colors[n])

print(min_needed)