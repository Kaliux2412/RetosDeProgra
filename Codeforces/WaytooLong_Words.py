import sys
num_words = int(sys.stdin.readline())
palabras = []
for n in range(0,num_words):
    word = list(sys.stdin.readline())
    word.pop(len(word)-1)
    palabras.append(word)
for p in range(0,len(palabras)):
    if len(palabras[p]) > 10:
        print(f'{palabras[p][0]}{(len(palabras[p]))-2}{palabras[p][len(palabras[p])-1]}')
    else:
        p = "".join(palabras[p])
        print(p)