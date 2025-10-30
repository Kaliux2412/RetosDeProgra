
def decimal_binario(num):
    lista_binario = []
    while num > 0:
        num = num // 2 
        lista_binario.append(num%2)
    ordenar = []
    for i in range ((len(lista_binario)-1), -1, -1):
        ordenar.append(lista_binario[i])
    print(ordenar)

p = "si"
while p == "si":
    numero= int(input("Elige un numero entero para convertir a binario: "))
    decimal_binario(numero)
    pregunta = input("quieres convertir otro numero? si/no: ")
    if pregunta == "si" or pregunta == "Si":
        p = "si"
    else:
        p = "no"
        print("Espero te haya servido! :)")
