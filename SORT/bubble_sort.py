def bubble_sort(data):
    for i in range(len(data)-1):
        swapped = False
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                if not swapped:
                    break

    return print(data)          



data = [5, 3, 8, 4, 2]
bubble_sort(data)