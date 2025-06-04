def f(word):
    lower_word = []
    for i in word:
        lower_word.append(i.lower())

    min = 0
    for i in range(1, len(word)):
        if lower_word[i] < lower_word[min]:
            min = i

    return word[min]

while True:
    n = int(input())
    if n == 0:
        break
    word = []
    for _ in range(n):
        word.append(input())

    print(f(word))