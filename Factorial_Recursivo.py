#Se hará una función que retorne un factorial de forma recursiva -FACIL

print("Bienvenido a la calculadora de factoriales!")
numero = int(input("Escribe el número que quieres sacar su factorial: "))

def factorial(num):
    if num == 0:
       return 1
    else:
        return num *factorial(num - 1)

resultado = factorial(numero)

print(f"El factorial de {numero} es: {resultado}")