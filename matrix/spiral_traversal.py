class Solution:
    def spirallyTraverse(self, mat):
        n = len(mat)
        m = len(mat[0])

        top = 0
        bottom = n - 1
        left = 0
        right = m - 1

        ans = []

        while top <= bottom and left <= right:

            # Left -> Right
            for j in range(left, right + 1):
                ans.append(mat[top][j])
            top += 1

            # Top -> Bottom
            for i in range(top, bottom + 1):
                ans.append(mat[i][right])
            right -= 1

            # Right -> Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    ans.append(mat[bottom][j])
                bottom -= 1

            # Bottom -> Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(mat[i][left])
                left += 1

        return ans
