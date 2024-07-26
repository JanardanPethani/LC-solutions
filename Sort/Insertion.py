def insertionSort(arr, i, n):
    if i == n:
        return
    j = i
    while j > 0 and arr[j] < arr[j - 1]:
        temp = arr[j - 1]
        arr[j - 1] = arr[j]
        arr[j] = temp
        j -= 1

    insertionSort(arr, i + 1, n)


arr = [1, 5, 3, 53, 2, 12, 1]

insertionSort(arr, 0, len(arr))
print(arr)
