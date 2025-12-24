import sys

n = int(sys.stdin.readline())
soldiers = list(map(int,sys.stdin.readline().split()))

general = False


def swap(list):
    count = 0
    n_max = list.index(max(list))
    n_min = list.index(min(list))
    
    while n_max != 0:
        list[n_max-1],list[n_max] = list[n_max],list[n_max-1]
        
        count +=1
        n_max -=1
    for n in range(0,len(list)):
        if list[n] == min(list):
            n_min = n
    while n_min != len(list)-1:
        list[n_min+1],list[n_min] = list[n_min],list[n_min+1]
       

        count +=1
        n_min +=1

    return count

print(swap(soldiers))


