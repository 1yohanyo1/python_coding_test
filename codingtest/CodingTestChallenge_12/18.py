from collections import deque

def bfs(start, graph, n):
    visited  = [False] * (n + 1)
    queue = deque()
    queue.append((start, 0))
    visited[start] = True # 상근이 번호 1번
    count = 0

    while queue:
        currnet, depth = queue.popleft()

        # bfs 탐색 깊이가 2가 되면 while문 탈출
        if depth == 2:
            break

        for i in graph[currnet]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, depth + 1))
                count += 1

    return count



n = int(input()) # 상근이의 동기 수
m = int(input()) # 리스트의 길이

graph = [[] for _ in range(n + 1)]

# 그래프 구현
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1, graph, n))