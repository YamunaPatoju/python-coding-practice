def arrange_amplifiers(arr):
    arr.sort()

    ones = arr.count(1)
    others = arr[ones:]

    return [1] * ones + others[::-1]


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    result = arrange_amplifiers(arr)
    print(*result)
