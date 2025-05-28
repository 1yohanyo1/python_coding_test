import sys
input = sys.stdin.readline

memoization = {}
def f(n):
    if n in memoization:
        return memoization[n]
    elif n == 1 or n == 2:
        return 1
    else:
        temp = f(n - 1) + f(n - 2)
        memoization[n] = temp
        return temp

n = int(input())
print(f(n))