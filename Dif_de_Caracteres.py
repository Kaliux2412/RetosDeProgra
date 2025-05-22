#Este programa analizará los caracteres diferentes de una cadena o palabra y 
#entregara aquellos que no aparezcan en ambas - FACIL

print("Bienvenido al Diferenciador de Caracteres!! :)")
def Diferenciar(str1,str2):
    lista1 = list(str1)
    lista2 = list(str2)
    out1 = []
    out2 = []
    
    for i in range(0,len(lista1)):
        if lista1.__contains__(lista1[i]) != lista2.__contains__(lista1[i]):
            out1.append(lista1[i])
    for n in range(0, len(lista2)):
        if lista2.__contains__(lista2[n]) != lista1.__contains__(lista2[n]):
            out2.append(lista2[n])
    print(out1,out2)
cad1 = input("Escribe tu primer cadena: ")
cad2 = input("Escribe tu segunda cadena: ")
Diferenciar(cad1,cad2)