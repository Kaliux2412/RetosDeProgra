import sys

s = sys.stdin.readline().lower()
s2 = sys.stdin.readline().lower()


if s<s2:
    print("-1")
elif s2 < s:
    print("1")
elif s2 ==s:
    print("0")