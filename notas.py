def maximize_sum_of_a():
    t = int(input().strip())  # Number of test cases
    
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        # Sort a ascending and b descending
        a.sort()
        b.sort(reverse=True)
        
        # Perform up to k swaps
        for i in range(min(k, n)):
            if a[i] < b[i]:
                a[i], b[i] = b[i], a[i]  # Swap to increase sum of a
            else:
                break  # No more beneficial swaps possible
        
        # Print final sum of a
        print(sum(a))


def maximize_string_value():
    # Read inputs
    s = input().strip()
    k = int(input().strip())
    weights = list(map(int, input().split()))  # 26 weights for a-z

    # Step 1: Calculate initial value of string s
    total_value = 0
    for i, char in enumerate(s, start=1):  # 1-based indexing
        total_value += weights[ord(char) - ord('a')] * i

    # Step 2: Find the maximum weight
    max_weight = max(weights)

    # Step 3: Add the value of k additional characters
    n = len(s)
    for i in range(1, k + 1):
        total_value += max_weight * (n + i)

    # Output the result
    print(total_value)


import sys

def max_books(n, t, a):
    l = 0
    current_sum = 0
    best = 0
    for r in range(n):
        current_sum += a[r]
        while current_sum > t and l <= r:
            current_sum -= a[l]
            l += 1
        # now current_sum <= t
        best = max(best, r - l + 1)
    return best

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    t = int(data[1])
    a = list(map(int, data[2:2+n]))
    print(max_books(n, t, a))

if __name__ == "__main__":
    main()
