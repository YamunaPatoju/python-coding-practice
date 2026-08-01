while True:
    a = list(map(int, input().split()))

    if a[0] == 0:
        break

    b = list(map(int, input().split()))

    arr1 = a[1:]
    arr2 = b[1:]

    i = j = 0
    sum1 = sum2 = 0
    ans = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sum1 += arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            sum2 += arr2[j]
            j += 1
        else:
            ans += max(sum1, sum2) + arr1[i]
            sum1 = 0
            sum2 = 0
            i += 1
            j += 1

    while i < len(arr1):
        sum1 += arr1[i]
        i += 1

    while j < len(arr2):
        sum2 += arr2[j]
        j += 1

    ans += max(sum1, sum2)

    print(ans)
