from collections import deque

def bfs(start, end):
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)

    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        current = queue.popleft()

        if current == end:
            return distance[current]
        
        for i in graph[current]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[current] + 1
                queue.append(i)
    
    return -1

n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


print(bfs(start, end))