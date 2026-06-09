def maxSubArraySum(arr):
    max_sum = arr[0]
    curr_sum = arr[0]

    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum
