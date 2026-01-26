
n = int(input())

phrase = ""

for l in range(1,n+1):
    if l > 1:
        phrase += "that "
    if l%2!=0:
        phrase += "I hate "
    else:
        phrase += "I love "

phrase += "it"
print(phrase)