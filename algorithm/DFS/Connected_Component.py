# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

# 예제 입력 1 
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 예제 출력 1 
# 2

def dfs(node):
    visited[node] = True  # 방문 표시
    for neighbor in graph[node]:  # 현재 노드와 연결된 노드들 탐색
        if not visited[neighbor]:  # 아직 방문 안 했으면
            dfs(neighbor)

# 입력 데이터
grid = [
    [6, 5],  # 첫 번째 줄: 정점 개수 N=6, 간선 개수 M=5
    [1, 2],
    [2, 5],
    [5, 1],
    [3, 4],
    [4, 6]
]

# 정점 개수와 간선 개수
N, M = grid[0]  

# 그래프 저장 (인접 리스트)
graph = {i: [] for i in range(1, N + 1)}

# 간선 정보 추가
for edge in grid[1:]:  # 첫 번째 줄 제외하고 간선 정보 저장
    u, v = edge
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프

# 방문 여부 체크 리스트
visited = [False] * (N + 1)
print(visited)

# 연결 요소 개수 세기
count = 0
for node in range(1, N + 1):
    if not visited[node]:  # 방문하지 않은 노드 발견 -> 새로운 연결 요소
        dfs(node)
        count += 1  # DFS 실행 횟수 = 연결 요소 개수

print(count)  # 연결 요소 개수 출력
