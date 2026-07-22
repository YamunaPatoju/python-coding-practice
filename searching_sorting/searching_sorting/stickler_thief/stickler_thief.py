class Solution:
    def findMaxSum(self, arr):
        prev2 = 0
        prev1 = 0

        for money in arr:
            curr = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = curr

        return prev1
