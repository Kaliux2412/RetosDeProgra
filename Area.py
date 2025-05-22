#Este codigo se encargará de sacar el área de triagulos, cuadrados o 
#rectangulos, con una sola función. FACIL

def Area(tipo, lado1, lado2):
    print("Bienvenido a la calculadora de Áreas")
    if tipo == "cuadrado":
        if lado1 != lado2:
            print("los lados de tu cuadrado deben ser iguales")
        else:
            area = lado1 * lado2
            
            print("El área de tu cuadrado es: " + str(area))
    if tipo == "rectangulo":
        if lado2 == lado1 or lado1 == lado2:
            print("Al ser un rectagulo un lado debe ser más grande que otro")
        else:
            area = lado2 * lado1
            print("El área de tu rectangulo es: " + str(area))
    if tipo == "triangulo":
        area = (lado1 * lado2)/2
        print("El área de tu triangulo es: " + str(area))

Area("rectangulo", 4, 9)