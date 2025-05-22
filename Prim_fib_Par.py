# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */
print("Bievenido al lector de números!")
num = int(input("Escribe un número: "))
def evaluar():
    lista = [0, 1]
    while len(lista) <= 1000:
        i = len(lista)
        suma = lista[i-2] + lista[i-1]
        x = suma
        lista.append(x)

    if(num not in lista):
        print("EL número no es fibonacci")
    else:
        print( str(num) +" es fibonacci")
    if(num % 2 == 0):
        print( str(num) + " es par")
    else:
        print( str(num) +" no es par")
    def primo():
        ar = []
        if(num < 2):
            print("Es primo")
            pri = ""
    
        for n in range (2, num):
            if(num % n == 0):
                pri = "f"
                ar.append(pri)
            else:
                pri = "t"
      
                ar.append(pri)
        f = "f"
        t = "t"

        if(t in ar and f not in ar):
            print("Es primo")

        else:
            print("No es primo")
            
    primo()
evaluar()
