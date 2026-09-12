class Solution:
    def maxSubtreeSum(self, root):
        self.ans = float('-inf')

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            total = left + right + node.data

            self.ans = max(self.ans, total)

            return total

        dfs(root)
        return self.ans
