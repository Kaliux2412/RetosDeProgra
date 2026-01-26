import sys

n = list(map(int,sys.stdin.readline().strip()))

four = n.count(4) 
seven = n.count(7)
if four + seven >1:
    if four+seven ==4 or four + seven ==7:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
