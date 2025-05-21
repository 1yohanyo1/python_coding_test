import sys
input = sys.stdin.readline

n = int(input())
string = [input().strip() for _ in range(n)]

sort_string_set = sorted(set(string)) # 중복 제거
sort_string = sorted(sort_string_set, key=len) # 길이 정렬

for i in range(len(sort_string)):
    print(sort_string[i])