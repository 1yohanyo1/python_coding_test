# 미리 계산산
MAX = 30
bottom_up = [[0] * MAX for _ in range(MAX)]

for i in range(MAX):
    bottom_up[i][0] = 1
    bottom_up[i][i] = 1

# 조합 점화식
for i in range(1, MAX):
    for j in range(1, i):
        bottom_up[i][j] = bottom_up[i-1][j-1] + bottom_up[i-1][j]

t = int(input())
for _ in range(t):
    # 서쪽
    n = int(input())
    # 동쪽
    m = int(input())
    print(bottom_up[m][n])
