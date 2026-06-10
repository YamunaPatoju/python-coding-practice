def getMinDiff(arr, k):
    n = len(arr)

    if n == 1:
        return 0

    arr.sort()

    ans = arr[n - 1] - arr[0]

    small = arr[0] + k
    big = arr[n - 1] - k

    if small > big:
        small, big = big, small

    for i in range(n - 1):
        mini = min(small, arr[i + 1] - k)
        maxi = max(big, arr[i] + k)

        if mini < 0:
            continue

        ans = min(ans, maxi - mini)

    return ans
