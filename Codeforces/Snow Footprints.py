n = int(input())
road = input()

# s = primer R
for i in range(n):
    if road[i] == 'R':
        s = i + 1
        break

# t depende de la última huella
for i in range(n - 1, -1, -1):
    if road[i] != '.':
        if road[i] == 'L':
            t = i      # i+1 - 1
        else:  # 'R'
            t = i + 2
        break

print(s, t)
