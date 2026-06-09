def rotate(arr):
    last = arr[-1]

    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last
    return arr
