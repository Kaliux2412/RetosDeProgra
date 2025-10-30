#plantilla base para entrada y salida rapida
import sys
from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect_right
import heapq

input = lambda: sys.stdin.readline().strip()
print = lambda x: sys.stdout.write(str(x) + "\n")

# Ejemplo: leer lista de enteros
# n = int(input())
# arr = list(map(int, input().split()))


#Busqueda binaria

from bisect import bisect_left, bisect_right

arr = [1, 3, 4, 7, 10]
x = 4

# Índice donde insertarías x para mantener orden
idx = bisect_left(arr, x)  
print(idx)  # Output: 2


#Bfs en un grafo tampoco creo usarlo

from collections import deque

def bfs(start, graph, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


# heap no creo usarlo

import heapq

def dijkstra(graph, start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, node = heapq.heappop(pq)
        if cost > dist[node]:
            continue
        for nxt, weight in graph[node]:
            if dist[node] + weight < dist[nxt]:
                dist[nxt] = dist[node] + weight
                heapq.heappush(pq, (dist[nxt], nxt))
    return dist

#para calcular sumas rapidas
arr = [1, 2, 3, 4]
prefix = [0] * (len(arr) + 1)

for i in range(1, len(arr) + 1):
    prefix[i] = prefix[i-1] + arr[i-1]

l, r = 1, 3
print(prefix[r+1] - prefix[l])

#uso de bisect

from bisect import bisect_left

arr = [1, 3, 5, 7, 9, 11, 13]
pos = bisect_left(arr, 9)

if pos != len(arr) and arr[pos] == 9:
    print("Encontrado en índice", pos)  # Output: 4
else:
    print("No encontrado")
