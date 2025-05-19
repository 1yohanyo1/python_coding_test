import sys
input = sys.stdin.readline

# heap_sort
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

def find_seven(arr):
    combination = [0] * 7
    found = False # Flag

    def dfs(idx, cnt, s):
        nonlocal found
        if found:
            return
        if cnt == 7:
            if s == 100:
                for h in combination:
                    print(h)
                found = True
            return
        if idx >= len(arr) or cnt + (len(arr) - idx) < 7:
            return
        if s > 100:
            return

        combination[cnt] = arr[idx]
        dfs(idx + 1, cnt + 1, s + arr[idx])
        dfs(idx + 1, cnt, s)

    dfs(0, 0, 0)

arr = [int(input()) for _ in range(9)]
heap_sort(arr)
find_seven(arr)
