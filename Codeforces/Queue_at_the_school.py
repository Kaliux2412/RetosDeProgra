import sys
def queue_after_t_seconds(n, t, s):
    queue = list(s)
    i = 0

    for _ in range(t):
        i = 0
        while i < n - 1:
            if queue[i] == 'B' and queue[i + 1] == 'G':

                queue[i], queue[i + 1] = queue[i + 1], queue[i]
                i += 1 
            i += 1


    
    return ''.join(queue)
n,t = map(int,sys.stdin.readline().split())
queue = sys.stdin.readline().strip()
resultado = queue_after_t_seconds(n,t,queue)
print(resultado)

