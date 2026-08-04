def merge(arr, left, mid, right):
    start2 = mid + 1

    # Already sorted
    if arr[mid] <= arr[start2]:
        return

    while left <= mid and start2 <= right:

        if arr[left] <= arr[start2]:
            left += 1
        else:
            value = arr[start2]
            index = start2

            # Shift elements to the right
            while index > left:
                arr[index] = arr[index - 1]
                index -= 1

            arr[left] = value

            left += 1
            mid += 1
            start2 += 1


def mergeSort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)

    merge(arr, left, mid, right)


# Driver Code
arr = [12, 11, 13, 5, 6, 7]

mergeSort(arr, 0, len(arr) - 1)

print(arr)
