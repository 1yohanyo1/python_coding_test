import sys
input = sys.stdin.readline

n = int(input())
students = []

for _ in range(n):
    name, dd, mm, yyyy = input().split()
    students.append([name, int(yyyy)*10000 + int(mm)*100 + int(dd)])

# 초기 값 설정
min, max = students[0][1], students[0][1]
min_name, max_name = students[0][0], students[0][0]

# 최대 최소 검색
for i in range(n):
    if students[i][1] < min:
        min = students[i][1]
        min_name = students[i][0]
    if students[i][1] > max:
        max = students[i][1]
        max_name = students[i][0]

print(max_name) # 가장 나이 어린 사람
print(min_name) # 가장 나이 많은 사람람