import sys
def love_string(s,k,w):
    # diccionario = {chr(i): i for i in range(97, 123)}
    suma = 0
    # for clave in diccionario:
    #     diccionario[clave] = 0

    n = len(s)
    for i in range(n):
        char_index = ord(s[i]) - ord('a')
        suma += w[char_index] * (i + 1)
    valor_max = max(w)
    # print(f"Claves con valor maximo {valor_max}:{claves_max}")
    suma_incial = k * n + k * (k + 1) // 2
    suma += valor_max*suma_incial
    # for f in range(n,k+n):
    #     s += claves_max[0]
    #     suma += valor_max*f
    print(suma)

s= list(sys.stdin.readline().strip())

k = int(sys.stdin.readline())
valores = list(map(int,sys.stdin.readline().split()))
for l in s:
    if l.isupper():
        print("Tienes mayusculas")
        s = []
        break
love_string(s,k,valores)

