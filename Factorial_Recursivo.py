<<<<<<< HEAD
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    

numero = int(input("Escribe el numero que quieras hacer factorial: "))
print(factorial(numero))
=======
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
>>>>>>> a33c377ff322d3f07ade8b9b1c406869616c6ace
