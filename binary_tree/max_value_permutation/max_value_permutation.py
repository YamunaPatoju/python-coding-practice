class Solution:
    def maxValue(self, arr):
        MOD = 10**9 + 7
        arr.sort()

        total = 0

        for i in range(len(arr)):
            total = (total + arr[i] * i) % MOD

        return total
