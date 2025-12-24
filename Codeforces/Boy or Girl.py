import sys

s = sys.stdin.readline().strip()

different_char = []

for c in s:
    if c not in different_char:
        different_char.append(c)
if len(different_char) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
