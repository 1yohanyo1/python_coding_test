from collections import deque

# 입력
n = int(input())

# BFS
def f(n):
    visited = [False] * (n + 1)
    queue = deque()
    queue.append((n, 0))
    visited[n] = True

    while queue:
        current, steps = queue.popleft()
        if current == 1:
            return steps
        
        next_nums = [current - 1]
        if current % 2 == 0:
            next_nums.append(current // 2)
        if current % 3 == 0:
            next_nums.append(current // 3)

        for next_num in next_nums:
            if next_num == 1:
                return steps + 1
            if not visited[next_num]:
                visited[next_num] = True
                queue.append((next_num, steps + 1))

print(f(n))
