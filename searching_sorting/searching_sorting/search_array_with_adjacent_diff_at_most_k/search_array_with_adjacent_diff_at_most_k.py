class Solution:
    def findStepKeyIndex(self, arr, k, x):
        i = 0
        n = len(arr)

        while i < n:
            if arr[i] == x:
                return i

            i += max(1, abs(arr[i] - x) // k)

        return -1
