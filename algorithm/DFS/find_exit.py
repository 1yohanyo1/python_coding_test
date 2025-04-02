# 📌 문제: 미로에서 출구 찾기
# 🔹 N x M 크기의 미로가 주어진다.
# 🔹 1은 이동할 수 있는 길, 0은 벽이다.
# 🔹 (0,0)에서 시작해서 (N-1, M-1)까지 갈 수 있는지 판단하라.
# 🔹 갈 수 있으면 "YES", 갈 수 없으면 "NO"를 출력하라.
maze = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1]
]

def dfs(i, j):
    # 위, 아래, 왼쪽, 오른쪽, 방문처리 인덱스가 0일 때 return
    if i < 0 or i >= len(maze) or j < 0 or j >= len(maze[0]) or maze[i][j] == 0:
        return False
    
    # 방문처리
    if maze[i][j] == 1:
        maze[i][j] = 0

    # 종료지점 도착 시
    if i == len(maze) - 1 and j == len(maze[0]) - 1:
        return True

    
    # 네 방향으로 탐색 (위, 아래, 왼쪽, 오른쪽)
    if dfs(i-1, j) or dfs(i+1, j) or dfs(i, j-1) or dfs(i, j+1):
        return True


if dfs(0, 0):
    print("YES")
else:
    print("NO")