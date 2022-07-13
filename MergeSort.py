from heapq import merge


def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2

        L = array[mid:]
        R = array[:mid]

        i = j = k = 0

        mergeSort(L)

        mergeSort(R)

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = L[j]
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
        