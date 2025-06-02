import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, visited, v):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

def count_islands(n, line):
    graph = [[] for _ in range(n + 1)]
    for u, v in line:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    count = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, visited, i)
            count += 1

    return count

# 입력 받기
n, m = map(int, input().split())
line = []
for _ in range(m):
    u, v = map(int, input().split())
    line.append([u, v])

print(count_islands(n, line))
