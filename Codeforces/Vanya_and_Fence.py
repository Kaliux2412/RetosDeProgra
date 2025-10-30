#Vanya and his friends are walking along the fence of height h and 
# they do not want the guard to notice them. In order to achieve this
#  the height of each of the friends should not exceed h. If the height of 
# some person is greater than h he can bend down and then he surely won't be noticed by the guard.
#  The height of the i-th person is equal to ai.
# Consider the width of the person walking as usual
#  to be equal to 1, while the width of the bent person is 
# equal to 2. Friends want to talk to each other while walking,
#  so they would like to walk in a single row. What is the minimum
#  width of the road, such that friends can walk in a row and remain unattended by the guard?

import sys
n,h = map(int,sys.stdin.readline().split())
a = list(sys.stdin.readline().split())
min_width = 0
for num in range(0,n):
    if int(a[num]) > h:
        min_width +=2
    else:
        min_width +=1
print(min_width)