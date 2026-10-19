class Solution:
    def findMinSum(self, a, b):
        a.sort()
        b.sort()

        total = 0

        for i in range(len(a)):
            total += abs(a[i] - b[i])

        return total
