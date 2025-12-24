import sys

s = list(map(str,sys.stdin.readline()))
l = len(s)
minus = 0
mayus = 0
for n in s:
    if n.islower():
        minus +=1
    elif n.isupper():
        mayus +=1
if mayus > minus:
    print(("".join(s)).upper())
elif mayus == minus or minus>mayus:
    print(("".join(s)).lower())

    