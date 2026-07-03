class Solution:
    def countOccurrence(self, mat, word):

        n = len(mat)
        m = len(mat[0])

        def dfs(i, j, idx):

            if i < 0 or i >= n or j < 0 or j >= m:
                return 0

            if mat[i][j] != word[idx]:
                return 0

            if idx == len(word) - 1:
                return 1

            ch = mat[i][j]
            mat[i][j] = '#'

            count = (
                dfs(i + 1, j, idx + 1) +
                dfs(i - 1, j, idx + 1) +
                dfs(i, j + 1, idx + 1) +
                dfs(i, j - 1, idx + 1)
            )

            mat[i][j] = ch

            return count

        ans = 0

        for i in range(n):
            for j in range(m):
                ans += dfs(i, j, 0)

        return ans
