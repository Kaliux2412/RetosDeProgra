import sys

year = sys.stdin.readline()
year1 = year.strip()

nuevo = []
listo = False
n =1
while listo == False:
    year = int(year) + n
    year1 = str(year).strip()
    unicos = []
    for c in year1:
        if c not in unicos:
            unicos.append(c)
    if len(unicos)< 4:
        listo = False
        nuevo = [year]
    else:
        listo = True
        print(("".join(unicos)))