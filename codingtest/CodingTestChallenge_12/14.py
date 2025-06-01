def cycles(derection, k):
    visited = [False] * (len(derection))
    count = 0
    current = 0

    while not visited[current]:
        visited[current] = True
        if current == k:
            return count
        current = derection[current]
        count+=1

    return -1    

n, k = map(int, input().split())
derection = []

for i in range(n):
    derection.append(int(input()))


print(cycles(derection, k))