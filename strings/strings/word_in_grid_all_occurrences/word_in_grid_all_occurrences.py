class Solution:
    def searchWord(self, mat, word):

        n = len(mat)
        m = len(mat[0])

        dirs = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        ans = []

        for i in range(n):
            for j in range(m):

                if mat[i][j] != word[0]:
                    continue

                for dx, dy in dirs:

                    x, y = i, j
                    k = 0

                    while k < len(word):
                        if x < 0 or x >= n or y < 0 or y >= m:
                            break
                        if mat[x][y] != word[k]:
                            break

                        x += dx
                        y += dy
                        k += 1

                    if k == len(word):
                        ans.append([i, j])
                        break

        return ans
