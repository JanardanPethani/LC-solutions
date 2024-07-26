def partition(arr, low, high):
    # Any indexd can be selected for pivot point
    print("low, high", low, high)
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        print(i, j)
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[low]
    arr[low] = arr[j]
    arr[j] = temp

    return j


def qs(arr, low, high):
    if low < high:
        pIdx = partition(arr, low, high)
        qs(arr, pIdx + 1, high)
        qs(arr, low, pIdx - 1)


arr = [1, 2, 2, 6, 4, 50, 10, 33]
qs(arr, 0, len(arr) - 1)
print(arr)
