import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    it = iter(data)
    n = int(next(it)); k = int(next(it))
    personas = sorted([int(next(it)) for _ in range(n)])
    bodegas = sorted([int(next(it)) for _ in range(k)])
    capacidad = [int(next(it)) for _ in range(k)]
    
    low, high = 0, 10**10
    ans = high
    
    def feasible(d):
        w_idx = 0
        cap_left = capacidad[:]
        for p in personas:
            while w_idx < k and bodegas[w_idx] < p - d:
                w_idx += 1
            if w_idx >= k:
                return False
            found = False
            temp_idx = w_idx
            while temp_idx < k and bodegas[temp_idx] <= p + d:
                if cap_left[temp_idx] > 0:
                    cap_left[temp_idx] -= 1
                    found = True
                    break
                temp_idx += 1
            if not found:
                return False
        return True
    
    while low <= high:
        mid = (low + high) // 2
        if feasible(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == "__main__":
    main()