#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

numero = 1
while(numero <= 100):
    if(numero % 3 == 0 or numero % 5 == 0):
        if(numero% 3 == 0 and numero % 5 == 0):
            print("FizzBuzz")
        else:
            if(numero % 3 == 0):
                print("Fizz")
            if(numero % 5 == 0):
                print("Buzz")
    else:
        print(numero)
    numero = numero + 1

    