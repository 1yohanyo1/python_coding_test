import sys
input = sys.stdin.readline

# 빙고 좌표 값 입력
position = {}
for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        position[row[j]] = (i, j)

# 사회자 호출
called_numbers = []
for _ in range(5):
    called_numbers += list(map(int, input().split()))

# 비트 마스크 연산 초기값
row_mask = [0] * 5
col_mask = [0] * 5
diag1_mask = 0
diag2_mask = 0


for idx, num in enumerate(called_numbers):
    x, y = position[num]

    # 해당 좌표 1로 채우기(가로, 세로 빙고)
    row_mask[x] |= (1 << y)
    col_mask[y] |= (1 << x)

    # x와 y가 같다면 1로 채우기기(왼->오 아래로 내려가는 대각선 빙고)
    if x == y:
        diag1_mask |= (1 << x)

    # x + y = 4라면 1로 채우기기(왼->오 위로 올라가는 대각선 빙고)
    if x + y == 4:
        diag2_mask |= (1 << x)

    bingo = 0
    for i in range(5):

        # 가로 빙고
        if row_mask[i] == 0b11111:
            bingo += 1
        
        # 세로 빙고
        if col_mask[i] == 0b11111:
            bingo += 1

    # 대각선 빙고
    if diag1_mask == 0b11111:
        bingo += 1
    if diag2_mask == 0b11111:
        bingo += 1

    if bingo >= 3:
        print(idx + 1)
        break