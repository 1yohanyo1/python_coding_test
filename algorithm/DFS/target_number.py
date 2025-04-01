def dfs(index, sum):
    global answer
    if index == len(numbers):
        if sum == target:
            answer += 1
        return
    
    dfs(index + 1, sum + numbers[index])
    dfs(index + 1, sum - numbers[index])

numbers = [1, 1, 1] 
target = 1
answer = 0

dfs(0, 0)

print(answer)