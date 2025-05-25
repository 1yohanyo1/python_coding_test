import sys
input = sys.stdin.readline

n = int(input())
size = []

for _ in range(n):
    height, weight = map(int, input().split())
    size.append((height, weight))

for i in range(len(size)):
    count = 1

    for j in range(len(size)):
        if i != j:
            if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
                count += 1

    print(count, end=' ')