
import random
longitud = int(input("Cuantos caracteres quieres que tenga? (escoge entre 8-16)\n"))
if(longitud >= 8 and longitud <=20): 
    def crear_contra(caracteres):
        contenido = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q", "R","S","T","U","V","W","X","Y","Z",
         "0","1","2","3","4","5","6","7","8","9","#","!","$","%","&","/","(",")","=","?",">","*","¡","¿"]
        con_mayus = input("Quieres que tenga mayúsculas?\n")
        con_num = input("Quieres que contenga números?\n")
        con_simbo = input("Y por último quieres que tenga símbolos?\n")

        def contador(op1, op2):
            num = 1
            contraseña = ""
            while num <= caracteres:
                aleatorio = random.randint(op1,op2)
                contraseña += contenido[aleatorio]
                num =  num + 1
            print(contraseña)
            
        if(con_mayus == "si" and con_num == "si" and con_simbo == "si"):
            contador(0,50)
        if(con_mayus == "si" and con_num == "si" and con_simbo == "no"):
            contador(0,36)
        if(con_mayus == "si" and con_num == "no" and con_simbo == "no"):
            contador(0,26)
        if(con_mayus == "no" and con_num == "si" and con_simbo == "no"):
            contador(27,36)
        if(con_mayus == "si" and con_num == "no" and con_simbo == "si"):
            num = 1
            contraseña = ""
            while num <= caracteres:
                aleatorio = random.randint(0,26)
                signoaleatorio = random.randint(37,50)
                escoger = random.randint(0,1)
                if(escoger == 0):
                    contraseña += contenido[aleatorio]
                if(escoger == 1):
                    contraseña += contenido[signoaleatorio]
                num =  num + 1
            print(contraseña)
        if(con_mayus == "no" and con_num == "si" and con_simbo == "si"):
            contador(27,50)
        if(con_mayus == "no" and con_num == "no" and con_simbo == "si"):
            contador(36,50)
        if(con_mayus == "no" and con_num == "no" and con_simbo == "no"):
            print("Debes de escoger una opción almenos")

else:
    print("Escoge entre 8 y 16, no más, no menos")
crear_contra(longitud)

