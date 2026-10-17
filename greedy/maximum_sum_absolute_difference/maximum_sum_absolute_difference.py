class Solution:
    def maxSumDifference(self, arr):
        arr.sort()
        n = len(arr)

        sequence = []
        left = 0
        right = n - 1

        while left < right:
            sequence.append(arr[left])
            sequence.append(arr[right])
            left += 1
            right -= 1

        if left == right:
            sequence.append(arr[left])

        total = 0

        for i in range(n - 1):
            total += abs(sequence[i] - sequence[i + 1])

        total += abs(sequence[-1] - sequence[0])

        return total
