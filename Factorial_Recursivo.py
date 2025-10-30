def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    

numero = int(input("Escribe el numero que quieras hacer factorial: "))
print(factorial(numero))