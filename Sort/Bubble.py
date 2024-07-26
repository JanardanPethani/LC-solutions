def bubble_sort(arr, last_idx):
    if last_idx == 1:
        return

    for idx in range(0, last_idx - 1):
        if arr[idx] > arr[idx + 1]:
            temp = arr[idx]
            arr[idx] = arr[idx + 1]
            arr[idx + 1] = temp

    bubble_sort(arr, last_idx - 1)


arr = [1, 4, 3, 2]
bubble_sort(arr, 4)
print(arr)
