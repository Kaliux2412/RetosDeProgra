import collections
import sys

def main():
    datos = sys.stdin.read().splitlines()
    n, m = map(int, datos[0].split())
    grilla = []
    inicio = None
    for i in range(1, n+1):
        line = datos[i].strip()
        grilla.append(list(line))
        if 'H' in line:
            j = line.index('H')
            inicio = (i-1, j)
    
    if not inicio:
        print(-1)
        return
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    visitas = set()
    queue = collections.deque()
    queue.append(inicio)
    visitas.add(inicio)
    
    queso_celdas = []
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if grilla[nx][ny] == 'Q' and (nx, ny) not in visitas:
                visitas.add((nx, ny))
                queue.append((nx, ny))
                queso_celdas.append((nx, ny))
    
    if not queso_celdas:
        print(-1)
        return
    
    quitar_min = float('inf')
    for celda in queso_celdas:
        x, y = celda
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grilla[nx][ny] == 'Q':
                count += 1
        quitar_min = min(quitar_min, count)
    
    print(quitar_min if quitar_min != float('inf') else -1)

if __name__ == "__main__":
    main()