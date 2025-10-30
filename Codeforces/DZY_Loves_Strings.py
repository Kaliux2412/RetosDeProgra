import sys
def love_string(s,k,w):
    # diccionario = {chr(i): i for i in range(97, 123)}
    suma = 0
    # for clave in diccionario:
    #     diccionario[clave] = 0

    n = len(s)
    for i in range(n):
        char_index = ord(s[i]) - ord('a')
        print(ord(s[i])-ord('a'))
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


# # Leer la entrada
# s = input().strip()
# k = int(input())
# weights = list(map(int, input().split()))

# # Calcular el valor inicial del string s
# total_value = 0
# n = len(s)

# for i in range(n):
#     char_index = ord(s[i]) - ord('a')
#     total_value += weights[char_index] * (i + 1)

# # Encontrar el peso máximo entre todas las letras
# max_weight = max(weights)

# # Las k letras adicionales se insertan al final
# # La primera letra insertada está en posición n+1, luego n+2, ..., n+k
# # La suma de estas posiciones es: (n+1) + (n+2) + ... + (n+k)
# # Esto se puede calcular como: k*n + (1 + 2 + ... + k) = k*n + k*(k+1)//2

# sum_of_positions = k * n + k * (k + 1) // 2

# # Agregar el valor de las letras insertadas
# total_value += max_weight * sum_of_positions

# print(total_value)