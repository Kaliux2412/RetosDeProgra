import sys
a,b,c,d = map(int,sys.stdin.readline().split())
if (1 <= a <= 100 and 
    1 <= b <= 100 and 
    1 <= c <= 100 and 
    1 <= d <= 10*12 and 
    c <= d):
    ardillas = 0
    semanas = 1
    while ardillas < d:

        ardillas = (c*a)+b
        c = ardillas
        if c > d:
            break
        else:
            semanas += 1
    print(semanas)
else:
    None