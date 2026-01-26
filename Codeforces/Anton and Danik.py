import sys

s = int(input())
n = list(map(str,sys.stdin.readline().strip()))


a = n.count("A")
d = n.count("D")

if a>d:
    print("Anton")
elif d>a:
    print("Danik")
else:
    print("Friendship")