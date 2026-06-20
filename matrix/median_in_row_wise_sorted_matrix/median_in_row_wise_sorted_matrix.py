class Solution:
    def median(self, mat):
        arr = []

        for row in mat:
            arr.extend(row)

        arr.sort()

        return arr[len(arr) // 2]
