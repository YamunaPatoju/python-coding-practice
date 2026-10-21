class Solution:
    def findMinDiff(self, arr, m):
        if m == 1:
            return 0

        arr.sort()
        minimum = float('inf')

        for i in range(len(arr) - m + 1):
            difference = arr[i + m - 1] - arr[i]
            minimum = min(minimum, difference)

        return minimum
