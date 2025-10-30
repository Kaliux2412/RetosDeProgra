<<<<<<< HEAD
codigo_morse = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G":"--.",
 "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q":"--.-", "R": ".-.", "S": "...", "T": "-","U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--","Z":"--..", " ": "  "}

def convertir_morse(frase):
    codigo = []
    arreglo = []
    texto = ''
    morse = ''
    for i in frase:
        if i.upper() in codigo_morse.keys():
            morse += codigo_morse[i.upper()]
        else:
             morse += i
        if i == "." or i == "-" or i == " ":
            codigo.append(i)
    print(morse)
    if codigo != "":
        letras_morse = ''
        for c in range(0,len(codigo)):
            if codigo[c] != ' ':
                letras_morse += codigo[c]
            else:
                arreglo.append(letras_morse)
                letras_morse = ''
        arreglo.append(letras_morse)
        for a in range(0,len(arreglo)):
            for clave,valor in codigo_morse.items():
                if arreglo[a] == valor: 
                    texto += clave        
        print(texto)

    
p = "si"
while p == "si":
    pregunta = input("Quieres traducir algo de Morse a texto o viceversa? si/no: ")
    if pregunta == "si" or pregunta == "Si":
        p = "si"
    elif pregunta == "no" or pregunta == "No":
        print("Gracias por usar traductor Morse :)")
        break
    else:
        print("Esa no es una opcion, escribe si o no")
        p = "si"
    frase = input("Escribe lo que quieras traducir: ")
    convertir_morse(frase)
    

    
=======
#En este codigo se logrará convertir cualquier texto a codigo morse 
#y viceversa - FACIL

print("¡Bienvenido al convertidor de CODIGO MORSE!")
traducir = "si"
while traducir == "si":
    def Morse(texto):
        codigo_morse = {"A":".-","B":"-...", "C": "-.-.","D":"-..","E":".","F":"..-.","G":"--.",
                        "H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","Ñ":"--.-",
                        "O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-",
                        "V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."," ":" "
                        }
        texto_morse = ""
        for letra in texto:
            if letra == "í": letra = "i"
            if letra =="ó": letra = "o"
            if letra == "ú": letra = "u"
            if letra == "á": letra = "a"
            if letra == "é": letra = "e"
            if letra.upper() in codigo_morse.keys():
                texto_morse += codigo_morse[letra.upper()]
            else:
                texto_morse += letra

        return texto_morse
    texto_escrito = input("Escribe lo que quieres convertir a morse: ")
    print(Morse(texto_escrito))
    otravez = input("Quieres traducir otra cosa?\n")
    if(otravez == "Si"or otravez == "si"):
        traducir = "si"
    else:
        traducir = "no" 
>>>>>>> a33c377ff322d3f07ade8b9b1c406869616c6ace
