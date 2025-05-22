#Un número de Armstrong, es todo aquel número que es la suma de cada uno de sus mismos dígitos
#elevado al número total de dígitos. Por ejemplo:
#- El número 153 es de Armstrong ya que este posee 3 dígitos y la suma de cada uno de sus dígitos
#elevado a 3 es igual a 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
#- El número 12 no es de Armstrong ya que la suma de los dígitos elevado al cuadrado es 1^2 + 2^2 = 5
#Elabore un algoritmo para encontrar todos los números de tipo Armstrong en el rango [a, b]. Los límites - MEDIO

digitos =[]
def Num_Armstrong(num):
    num_original = num
    while num > 0:
        digitos.append(num % 10 )
        num = num // 10
    num_separado = digitos[::-1]
    lista_num_elevado = []
    for n in range(0,len(num_separado)):
        num_elevado = num_separado[n]**len(num_separado)
        lista_num_elevado.append(num_elevado)
    sum = 0
    for l in range(0,len(lista_num_elevado)):
        sum = sum + (lista_num_elevado[l])
    if (sum == num_original):
        print(f"El número {num_original} es un número de Armstrong\n ya que la suma de sus digitos elevados a la cantidad de esos mismos digitos es igual al mismo número: {num_original}")
    else:
        print("Este no es un número de Armstrong")
print("Bienvenido a el agente de números de Armstrong")
numero = int(input("Escribe el número que deseas evaluar: "))
Num_Armstrong(numero)
