import sys

n = int(sys.stdin.readline())

magnets = []
for m in range(0,n):
    ma = int(sys.stdin.readline())
    magnets.append(ma)

groups = 0

atraction = ""

for m in range(1,len(magnets)):
    if magnets[m-1] == magnets[m]:
        atraction = "attracted"
    else:
        atraction = "repelled"
        groups+=1
print(groups+1)