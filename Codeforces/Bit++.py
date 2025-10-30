n = int(input())
x = 0
for i in range(n):
    s = input()
    if s == "++X" or s == "X++":
        x+=1
    elif s == "--X" or "X--":
        x -=1
    else:
        print("Esa no es una opcion")
        break
print(x)