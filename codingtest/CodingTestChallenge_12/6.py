import sys
input = sys.stdin.readline

n = list(map(int, input().split()))

while 1:
    swaped = False
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            n[i], n[i+1] = n[i+1], n[i]
            print(*n)
            swaped = True
    if not swaped:
        break
        

