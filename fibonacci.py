# /*
#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...
#  */

def fibonacci():
    lista = [0, 1]
<<<<<<< HEAD
    while len(lista) <= 1000:
=======
    while len(lista) <= 100:
>>>>>>> a33c377ff322d3f07ade8b9b1c406869616c6ace
        i = len(lista)
        suma = lista[i-2] + lista[i-1]
        x = suma
        lista.append(x)
    print(lista)
fibonacci()
