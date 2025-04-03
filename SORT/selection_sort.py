def selection_sort(data):

    for i in range(len(data)-1):
        min = i
        for j in range(i + 1, len(data)):
            if data[min] > data[j]:
                min = j
        data[i], data[min] = data[min], data[i]


    return print(data)



data = [5, 3, 8, 4, 2]
selection_sort(data)