################## A. Insomnia cure ##########################


#«One dragon. Two dragon. Three dragon», — the princess was counting. She had trouble falling asleep, and she got bored of counting lambs when she was nine.
#However, just counting dragons was boring as well, so she entertained herself at best she could. Tonight she imagined that all dragons were here to steal her, and she was fighting them off. Every k-th dragon got punched in the face with a frying pan. Every l-th dragon got his tail shut into the balcony door. Every m-th dragon got his paws trampled with sharp heels. Finally, she threatened every n-th dragon to call her mom, and he withdrew in panic.
#How many imaginary dragons suffered moral or physical damage tonight, if the princess counted a total of d dragons?


################***Input***###############

#$$$$$ Input data contains integer numbers k, l, m, n and d, each number in a separate line (1 ≤ k, l, m, n ≤ 10, 1 ≤ d ≤ 105).

################***Output***################

#$$$$$ Output the number of damaged dragons.



import sys

k = int(sys.stdin.readline())
l = int(sys.stdin.readline())
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
d = int(sys.stdin.readline())

dam_dragons = 0
for v in range(1,d+1):
    if v== k or v%k ==0:
        dam_dragons +=1
    elif v== l or v%l ==0:
        dam_dragons +=1
    elif v== m or v%m ==0:
        dam_dragons +=1
    elif v== n or v%n ==0:
        dam_dragons +=1

print(dam_dragons)