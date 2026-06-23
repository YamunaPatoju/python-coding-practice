class Solution:
    def findMaxValue(self, n, mat):

        maxArr = [[0] * n for _ in range(n)]

        maxArr[n - 1][n - 1] = mat[n - 1][n - 1]

        for j in range(n - 2, -1, -1):
            maxArr[n - 1][j] = max(mat[n - 1][j], maxArr[n - 1][j + 1])

        for i in range(n - 2, -1, -1):
            maxArr[i][n - 1] = max(mat[i][n - 1], maxArr[i + 1][n - 1])

        ans = float('-inf')

        for i in range(n - 2, -1, -1):
            for j in range(n - 2, -1, -1):

                ans = max(ans, maxArr[i + 1][j + 1] - mat[i][j])

                maxArr[i][j] = max(
                    mat[i][j],
                    maxArr[i][j + 1],
                    maxArr[i + 1][j]
                )

        return ans
