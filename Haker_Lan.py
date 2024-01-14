# /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  */
print("Bienvenido al Traductor de Hakers!")
traducir = input("Quieres traducir algo? ")
while traducir == "Si" or traducir == "si":
    def haker_language(frase):
        leet = {"A":"4","B": "I3","C": "[","D": ")","E": "3", "F": "|=", "G": "&", "H": "#", "I": "1", "J": ",_|", "K": ">|", "L": "1", 
                "M": "/\/\\", "N": "^/", "O": "0", "P": "|*", "Q": "(_,)", "R": "I2", "S": "5", "T": "7","U": "(_)",
                "V":"\/", "W": "\/\/", "X":"><", "Y": "j", "Z":"2"
                }
        leet_frase = ""
        for letra in frase:
            if letra.upper() in leet.keys():
                leet_frase += leet[letra.upper()]
            else:
                leet_frase += letra
        return leet_frase
    palabra = input("Escribe lo que quieres traducir: ")
    print(haker_language(palabra))
    otravez = input("Quieres traducir otra cosa?\n")
    if(otravez == "Si"or otravez == "si"):
        traducir = "si"
    else:
        traducir = "no"
print("FIN DEL PROGRAMA")



