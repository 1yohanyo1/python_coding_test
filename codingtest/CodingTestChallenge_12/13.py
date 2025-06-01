def cycles(P):
    # 방문 노드 초기화
    visited = [False] * (len(P) + 1)
    count = 0

    for i in range(1, len(P)):
    	# 방문한 노드는 pass
        if not visited[i]:
            count += 1
            current = i

            # 사이클이 끝날 때 까지 탐색
            while not visited[current]:
                visited[current] = True
                current = P[current]
    return count

T = int(input())
for _ in range(T):
    N = int(input()) 
    P = [0] + list(map(int, input().split())) # 순열
    print(cycles(P))