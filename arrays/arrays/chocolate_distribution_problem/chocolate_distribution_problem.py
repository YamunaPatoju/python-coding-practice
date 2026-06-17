def findMinDiff(self, arr, m):
        arr.sort()

        min_diff = float('inf')

        for i in range(len(arr) - m + 1):
            diff = arr[i + m - 1] - arr[i]
            min_diff = min(min_diff, diff)

        return min_diff
