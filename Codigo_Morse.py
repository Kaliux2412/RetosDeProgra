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