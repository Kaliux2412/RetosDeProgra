
def main():
    n = int(input().strip())
    palabraunica = []
    cuenta_de_palabras_persona = []
    
    for _ in range(n):
        p = int(input().strip())
        cuenta = {}
        palabras_unica = set()
        for _ in range(p):
            word = input().strip()
            cuenta[word] = cuenta.get(word, 0) + 1
            palabras_unica.add(word)
        palabraunica.append(palabras_unica)
        cuenta_de_palabras_persona.append(cuenta)
    palabras_comunes = set(palabraunica[0])
    for i in range(1, n):
        palabras_comunes &= palabraunica[i]
    print(palabras_comunes)
    if not palabras_comunes:
        return
    
    lista_frecuencia = []
    for word in palabras_comunes:
        frec_total = 0
        for cuenta in cuenta_de_palabras_persona:
            frec_total += cuenta.get(word, 0)
        lista_frecuencia.append((frec_total, word))
    
    sorted_list = sorted(lista_frecuencia, key=lambda x: (x[0], x[1]), reverse=True)
    
    for freq, word in sorted_list:
        print(word)

if __name__ == "__main__":
    main()