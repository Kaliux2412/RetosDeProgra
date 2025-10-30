import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index+1])
        index += 2
        points.append((x, y))
    
    midpoints = {}
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            mid_x = x1 + x2
            mid_y = y1 + y2
            key = (mid_x, mid_y)
            if key in midpoints:
                midpoints[key].append((i, j))
            else:
                midpoints[key] = [(i, j)]
    
    for key, segments in midpoints.items():
        if len(segments) >= 2:
            print("YES")
            return
    
    print("NO")

if __name__ == "__main__":
    main()