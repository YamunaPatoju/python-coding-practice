class Solution:
    def solveWordWrap(self, arr, k):

        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = float('inf')
            length = 0

            for j in range(i, n):

                length += arr[j]

                if length + (j - i) > k:
                    break

                if j == n - 1:
                    cost = 0
                else:
                    extra = k - (length + (j - i))
                    cost = extra * extra + dp[j + 1]

                dp[i] = min(dp[i], cost)

        return dp[0]
