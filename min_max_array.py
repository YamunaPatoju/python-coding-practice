def getMinMax(arr):
    min_ele = arr[0]
    max_ele = arr[0]

    for num in arr:
        if num < min_ele:
            min_ele = num

        if num > max_ele:
            max_ele = num

    return min_ele, max_ele


arr = [3, 5, 1, 8, 2]
minimum, maximum = getMinMax(arr)

print("Minimum:", minimum)
print("Maximum:", maximum)
