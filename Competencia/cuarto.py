import sys
def main():
    valor = sys.stdin.read().splitlines()
    n, m = map(int, valor[0].split())
    grid = []
    for i in range(1, 1 + n):
        line = valor[i].strip()
        grid.append(list(line))  
    
    min_row = n
    max_row = 0
    min_col = m
    max_col = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                if i < min_row:
                    min_row = i
                if i > max_row:
                    max_row = i
                if j < min_col:
                    min_col = j
                if j > max_col:
                    max_col = j
    
    if min_row == n:
        print("Triple Corolla Flower")  
        return
    
    rows = max_row - min_row + 1
    cols = max_col - min_col + 1
    reducida = []
    for i in range(min_row, max_row + 1):
        row = []
        for j in range(min_col, max_col + 1):
            row.append(grid[i][j])
        reducida.append(row)
    
    if reducida[0][cols-1] == '.':
        print("Double Petal Flower")
    else:
        print("Triple Corolla Flower")

if __name__ == "__main__":
    main()