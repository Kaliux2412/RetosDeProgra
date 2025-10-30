w = list(map(str,input().strip()))
nueva = ""
for n in range(0,len(w)):
    if n == 0:
        nueva+=w[n].upper()
    else:
        nueva += w[n]
print(nueva)