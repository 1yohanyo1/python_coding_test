#  문제: 섬의 개수 구하기 🌊
# 0과 1로 이루어진 2D 그리드(지도)가 주어질 때, 1로 이루어진 "섬" 의 개수를 구하는 함수를 작성하시오.
# 섬은 상하좌우로 연결된 1의 그룹이며, 대각선으로 연결된 경우는 다른 섬으로 간주합니다.

# grid = [
#     [1, 1, 0, 0, 0],
#     [1, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 1]
# ]

# 예제 출력:
# 3

def numIslands(grid):
    if not grid:
        return 0

    def dfs(i, j):
        # 위로 빠지거나 or 아래로 빠지거나 or 왼쪽으로 빠지거나 or 오른쪽으로 빠지거나 or 해당 인덱스가 0이면 return(재귀)
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return
        
        # 현재 위치 방문 처리 (1 → 0 변경)
        grid[i][j] = 0  

        # 상, 하, 좌, 우 네 방향 탐색
        dfs(i - 1, j)  # 위
        dfs(i + 1, j)  # 아래
        dfs(i, j - 1)  # 왼쪽
        dfs(i, j + 1)  # 오른쪽

    island_count = 0  # 섬 개수 카운트

    # 2차원 리스트 순회하며 DFS 실행
    for i in range(len(grid)): # Y 좌표
        for j in range(len(grid[0])): # X 좌표
            if grid[i][j] == 1:  # 섬을 발견하면 DFS 실행
                dfs(i, j)
                island_count += 1  # DFS가 끝나면 섬 개수 증가

    return island_count

grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]

print(numIslands(grid))