import sys
input = sys.stdin.readline

n = int(input()) 
members = []

for _ in range(n):
    age, name = input().split()
    members.append((int(age), name))

members.sort(key=lambda x: (x[0])) # 이름 정렬

for age, name in members:
    print(age, name)