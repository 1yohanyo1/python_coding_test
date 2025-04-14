# 1. a, b, c의 갯수가 주어진다.
# 2. 갯수에 따라 가장 작은 문자열을 만든다.
# 3. 단, 3개 이상의 같은 문자가 이어지면 안 된다.
# ex) a = 1, b = 3, c = 3
# => a b c c b c
# ex) a = 1, b = 4, c = 0
# => b a b b

from collections import deque

def generate_min_string_iterative_dp(a_max, b_max, c_max):
    dp = {}
    queue = deque()

    dp[(0, 0, 0, '', '')] = ''
    queue.append((0, 0, 0, '', ''))

    while queue:
        a, b, c, last1, last2 = queue.popleft()
        current = dp[(a, b, c, last1, last2)]

        for ch in ['a', 'b', 'c']:
            if ch == 'a' and a < a_max:
                na, nb, nc = a + 1, b, c
            elif ch == 'b' and b < b_max:
                na, nb, nc = a, b + 1, c
            elif ch == 'c' and c < c_max:
                na, nb, nc = a, b, c + 1
            else:
                continue

            if last1 == last2 == ch:
                continue

            new_key = (na, nb, nc, last2, ch)
            new_str = current + ch

            if new_key not in dp or new_str < dp[new_key]:
                dp[new_key] = new_str
                queue.append(new_key)

    results = [v for (a, b, c, _, _), v in dp.items() if a == a_max and b == b_max and c == c_max]
    return min(results) if results else ""





print(generate_min_string_iterative_dp(1, 1, 7))
print(generate_min_string_iterative_dp(3, 8, 8))
print(generate_min_string_iterative_dp(80, 3, 80))
print(generate_min_string_iterative_dp(50, 100, 303))
# print(generate_min_string_iterative_dp(500, 500, 500))