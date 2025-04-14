# 1. a, b, c의 갯수가 주어진다.
# 2. 갯수에 따라 가장 작은 문자열을 만든다.
# 3. 단, 3개 이상의 같은 문자가 이어지면 안 된다.
# ex) a = 1, b = 3, c = 3
# => a b c c b c
# ex) a = 1, b = 4, c = 0
# => b a b b

def generate_min_string(a, b, c):
    total_len = a + b + c
    best_result = None
    found = False

    def backtrack(path, a_left, b_left, c_left):
        nonlocal best_result, found

        if len(path) == total_len:
            best_result = ''.join(path)
            found = True
            return

        for ch, count_left in [('a', a_left), ('b', b_left), ('c', c_left)]:
            if count_left == 0:
                continue

            if len(path) >= 2 and path[-1] == path[-2] == ch:
                continue

            path.append(ch)
            if ch == 'a':
                backtrack(path, a_left - 1, b_left, c_left)
            elif ch == 'b':
                backtrack(path, a_left, b_left - 1, c_left)
            else:
                backtrack(path, a_left, b_left, c_left - 1)

            if found:
                return

            path.pop()

    backtrack([], a, b, c)
    return best_result if best_result else "no answer"



print(generate_min_string(1, 1, 7))
print(generate_min_string(3, 8, 8))
# print(generate_min_string(30, 80, 80))