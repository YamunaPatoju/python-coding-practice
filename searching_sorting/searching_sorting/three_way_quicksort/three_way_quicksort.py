def threeWayPartition(arr, low, high):
    if low >= high:
        return

    pivot = arr[low]

    lt = low
    i = low
    gt = high

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1

        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1

        else:
            i += 1

    threeWayPartition(arr, low, lt - 1)
    threeWayPartition(arr, gt + 1, high)


# Driver Code
arr = [4, 9, 4, 4, 2, 7, 4, 1]

threeWayPartition(arr, 0, len(arr) - 1)

print(arr)
