from bisect import bisect_left, bisect_right

n, A, B = map(int, input().split())

arr = [int(input()) for _ in range(n)]

mid = n // 2

left = arr[:mid]
right = arr[mid:]


def generate(nums):
    sums = []
    m = len(nums)

    for mask in range(1 << m):
        total = 0

        for i in range(m):
            if mask & (1 << i):
                total += nums[i]

        sums.append(total)

    return sums


leftSums = generate(left)
rightSums = generate(right)

rightSums.sort()

ans = 0

for x in leftSums:
    low = A - x
    high = B - x

    l = bisect_left(rightSums, low)
    r = bisect_right(rightSums, high)

    ans += (r - l)

print(ans)
