# 최대값 생성
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
    n, m = map(int, input().split())
    print(bottom_up[m][n])