import sys
nombre = list(sys.stdin.readline())
nombre.pop(len(nombre)-1)
if ((len(nombre))-1) < 10:
    print(f"Hello {"".join(nombre)}!")