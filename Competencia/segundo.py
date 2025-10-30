import sys
cadena = list(sys.stdin.readline())
if cadena.count("T") == cadena.count("C") == cadena.count("S"):
    print("YES")
else:
    print("NO")