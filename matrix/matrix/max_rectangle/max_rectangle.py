class Solution:
    def maxArea(self, mat):
        def largestRectangle(heights):
            stack = []
            max_area = 0
            n = len(heights)

            for i in range(n + 1):
                curr = 0 if i == n else heights[i]

                while stack and heights[stack[-1]] > curr:
                    h = heights[stack.pop()]

                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i

                    max_area = max(max_area, h * width)

                stack.append(i)

            return max_area

        cols = len(mat[0])
        heights = [0] * cols
        ans = 0

        for row in mat:
            for j in range(cols):
                if row[j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            ans = max(ans, largestRectangle(heights))

        return ans
