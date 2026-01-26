def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort()
    
    if k > n:
        print(-1)
        return
    
    if k == 0:
        m = a[-1] + 1
        print(m, 0)
        return
    
    m = a[n - k]
    
    if n - k - 1 >= 0 and a[n - k - 1] == m:
        print(-1)
        return
    
    print(m, 0)
solve()