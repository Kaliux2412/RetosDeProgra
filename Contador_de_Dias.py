from datetime import datetime
def calcular_dias(fecha1,fecha2):
    formato = datetime.now().strftime('%d/%m/%Y')
    primera = []
    segunda = []
    arreglada = []
    dias = 0
    for f in fecha1:
        primera.append(f)
    for f in fecha2:
        segunda.append(f)
    f1 = ''
    for i in range(0,len(fecha2)):
        if primera[i] != "/":
            f1 += primera[i]
        else:
            arreglada.append(f1)
            f1 = ''
    arreglada.append(f1)

    f1 = ''
    for i in range(0,len(fecha2)):
        if segunda[i] != "/":
            f1 += segunda[i]
        else:
            arreglada.append(f1)
            f1 = ''
    arreglada.append(f1)
    for n in range(0, len(arreglada)):
        arreglada[n] = int(arreglada[n])
    u = 0
    if arreglada[u] < arreglada[u+3] == True:
        dias = dias + ((arreglada[u+3])-(arreglada[u]))
    else:
       dias = dias + ((arreglada[u])-(arreglada[u+3]))
    if arreglada[u+1] < arreglada[u+4] == True:
        dias = dias + (((arreglada[u+4])-(arreglada[u+1]))*30)
    else:
       dias = dias + (((arreglada[u+1])-(arreglada[u+4]))*30)
    if arreglada[u+2] < arreglada[u+5] == True:
        dias = dias + (((arreglada[u+5])-(arreglada[u+2]))*365)
    else:
       dias = dias + (((arreglada[u+2])-(arreglada[u+5]))*365)
        
    print(f'La diferencia en dias es de {dias} dias')
            

fecha1 = input("Escribe tu primer fecha: ")
fecha2 = input("Escribe tu segunda fecha: ")
calcular_dias(fecha1,fecha2)