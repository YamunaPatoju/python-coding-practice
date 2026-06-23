class Solution:
    def kthSmallest(self, mat, k):
        arr = []

        for row in mat:
            arr.extend(row)

        arr.sort()

        return arr[k - 1]
