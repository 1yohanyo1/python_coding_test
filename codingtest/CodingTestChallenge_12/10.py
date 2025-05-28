import sys
input = sys.stdin.readline

testcase = int(input())

memo = {}
def f(k, n):
    if (k, n) in memo:
        return memo[(k, n)]
    if k == 0:
        return n
    if n == 1:
        return 1
    temp = f(k, n - 1) + f(k - 1, n)
    memo[(k, n)] = temp
    return temp

for _ in range(testcase):
    k = int(input())
    n = int(input())
    print(f(k, n))
