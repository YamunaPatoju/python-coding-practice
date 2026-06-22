class Solution:
    def sortedMatrix(self, mat):
        arr = []

        for row in mat:
            arr.extend(row)

        arr.sort()

        n = len(mat)
        k = 0

        for i in range(n):
            for j in range(n):
                mat[i][j] = arr[k]
                k += 1

        return mat
