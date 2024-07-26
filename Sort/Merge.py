def mergeSortv2(array):
    if len(array) > 1:
        #  r is the point where the array is divided into two subarrays
        r = len(array) // 2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSortv2(L)
        mergeSortv2(M)

        left = right = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while left < len(L) and right < len(M):
            if L[left] < M[right]:
                array[k] = L[left]
                left += 1
            else:
                array[k] = M[right]
                right += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while left < len(L):
            array[k] = L[right]
            right += 1
            k += 1

        while right < len(M):
            array[k] = M[right]
            right += 1
            k += 1


arr = [3, 1, 2, 4]


mergeSortv2(arr)
print(arr)
