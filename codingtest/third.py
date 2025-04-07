# 1. 각각 N개의 정수로 구성된 두 개의 배열 A와 B를 받는다. 그리고 이 두 배열을 C로 병합하려고 한다.
# 2. 각 인덱스 K(0 ~ N-1) 에 대해 C[k] 또는 B[k]가 될 수 있다
# ex) A = [1, 2, 4, 3] 및 B = [1, 3, 2, 3] 다음과 같은 방식으로 병합될 수 있다. 그러면 C = [1, 3, 4, 3]  / [B, B, A, B] 가 들어간거임
# 우리의 목표는 C에 존재하지 않는 가장 작은 양의 정수가 가능한 작은 배열 C를 얻는 것이다.
# 위의 예에서 우리는 C = [1, 3,4,3 ]을 만들 수 있으며 결과는 2이다. 왜냐면 C에서 제외되는 가장 작은 양의 정수가 2이기 때문이다.

# 길이가 N인 두 개의 정수 배열 A와 B가 주어졌을 때, 배열 C에 존재하지 않는 갖아 작은 양의 정수를 반환하는 것이다. 배열 C는 배열 A or B 에서 요소를 선택하여 생성

# Ex) A = [1, 2, 4, 3]이고 B = [1, 3, 2, 3] 인 경우 함수는 위에서 설명한 대로 2를 반환
# 2. A = [3, 2, 1, 6, 5] 이고 B = [4, 2, 1, 3, 3]인 경우 함수는 3을 반환 C = [4, 2, 1, 6, 5]를 생성 [B, A, B , A, A]
# 3. A = [1, 2] 이고 B = [1, 2]인 경우 함수는 3을 반환해야한다. C = [1. 2]를 만들 수 있다 [A, B] 

# 문제
# 1. N(1 ... 100000) 범위 내의 정수이다.
# 2. 배열 A와 B의 요소는 [1 ... 100000] 범위 내의 정수
# 3. 입력 배열의 크기가 동일하다.

def find_missing_integer(A, B):
    N = len(A)
    C = []
    used_numbers = set()

    # C2: A[i] == B[i] 인 경우 저장
    priority_values = set()
    for i in range(N):
        if A[i] == B[i]:
            priority_values.add(A[i])

    for i in range(N):
        a, b = A[i], B[i]

        # 먼저 C2(priority_values)에 있는 값이면 그걸 선택
        if a in priority_values and a not in used_numbers:
            chosen = a
        elif b in priority_values and b not in used_numbers:
            chosen = b
        # C2에 없는 경우 기존 방식대로 선택
        elif a in used_numbers and (b in used_numbers or a > b):
            chosen = a
        elif b in used_numbers:
            chosen = b
        else:
            chosen = max(a, b)

        C.append(chosen)
        used_numbers.add(chosen)

    # C에 없는 가장 작은 양의 정수 찾기
    missing = 1
    while missing in used_numbers:
        missing += 1

    return missing


print(find_missing_integer([1, 3, 4, 5, 7, 6, 2], [1, 2, 4, 5, 6, 3, 2]))  # ✅ 예상: 3
print(find_missing_integer([1, 2, 4, 3], [1, 3, 2, 3]))                    # ✅ 예상: 2
print(find_missing_integer([3, 2, 1, 6, 5], [4, 2, 1, 3, 3]))              # ✅ 예상: 3
print(find_missing_integer([1, 2], [1, 2]))                                # ✅ 예상: 3
print(find_missing_integer([5, 6, 7], [8, 9, 10]))                         # ✅ 예상: 1
print(find_missing_integer([1, 2, 3], [4, 5, 6]))                          # ✅ 예상: 1
print(find_missing_integer([1, 3, 4, 5, 7, 6, 2], [1, 2, 4, 5, 6, 3, 2]))  # ✅ 예상: 3