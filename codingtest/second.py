# 1. a, b, c의 갯수가 주어진다.
# 2. 갯수에 따라 가장 작은 문자열을 만든다.
# 3. 단, 3개 이상의 같은 문자가 이어지면 안 된다.
# ex) a = 1, b = 3, c = 3
# => a b c c b c
# ex) a = 1, b = 4, c = 0
# => b a b b

from functools import lru_cache

def generate_min_string_dp(a, b, c):
    total_len = a + b + c

    @lru_cache(maxsize=None)
    def dfs(a_left, b_left, c_left, last1, last2):
        if a_left == 0 and b_left == 0 and c_left == 0:
            return ""

        for ch, cnt in [('a', a_left), ('b', b_left), ('c', c_left)]:
            if cnt == 0:
                continue
            if last1 == last2 == ch:
                continue

            if ch == 'a':
                suffix = dfs(a_left - 1, b_left, c_left, last2, 'a')
            elif ch == 'b':
                suffix = dfs(a_left, b_left - 1, c_left, last2, 'b')
            else:
                suffix = dfs(a_left, b_left, c_left - 1, last2, 'c')

            if suffix is not None:
                return ch + suffix

        return None

    result = dfs(a, b, c, '', '')
    return result if result is not None else "no answer"




print(generate_min_string_dp(1, 1, 7))
print(generate_min_string_dp(3, 8, 8))
print(generate_min_string_dp(80, 3, 80))
print(generate_min_string_dp(50, 100, 303))
# print(generate_min_string_dp(500, 500, 500))