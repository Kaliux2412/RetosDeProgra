#En este reto se creara un convertidor de numeros decimales a binario
#-DIFICIL

print("Bienvenido al convertidor de números decimales a binarios")

def Binary():
    eleccion = input("Quieres convertir un número a binario (escribe B si es así) o al revés (escribe N): ")
    if eleccion == "B" or eleccion == "b":
        numero =  int(input("Escribe el número que quieres convertir a binario: "))
        lista_residuos = []
        while numero > 0:
            residuo = numero%2
            lista_residuos.append(int(residuo))
            if numero%2 == 1:
                numero = numero-1
            numero = numero/2
        lista_binaria = lista_residuos[::-1]
        print(f"Tu número en binario es: ")
        print(lista_binaria)
    else:
        list_combinacion = list(input("Escribe la combinación binaria: "))
        list_int = []
        for n in range(0,len(list_combinacion)):
            convertir = int(list_combinacion[n])
            if convertir > 1:
                print("Esa no es una combanción binaria")
                break
            else:
                list_int.append(convertir)
                list_binario = list_int[::-1]
                lista_final = []
                for i in range(0, len(list_binario)):
                    indice = ((list_binario[i])*2)**i
                    lista_final.append(indice)
        sum = 0
        for b in range(0, len(lista_final)):
            sum = sum + lista_final[b]
        print(f"El número oculto en esta combinación es: {sum-1}")
        

Binary()
r = True
while r == True:
    repetir = input("quieres evaluar otro número?: ")
    if repetir == "si":
        Binary()
        r = True
    else:
        print("Espero te haya sido útil :)")
        r = False


