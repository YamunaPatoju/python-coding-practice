class Solution:
    def sumOfLongRootToLeafPath(self, root):
        self.maxLen = 0
        self.maxSum = 0

        def dfs(node, length, total):
            if node is None:
                return

            length += 1
            total += node.data

            if node.left is None and node.right is None:
                if length > self.maxLen:
                    self.maxLen = length
                    self.maxSum = total
                elif length == self.maxLen:
                    self.maxSum = max(self.maxSum, total)
                return

            dfs(node.left, length, total)
            dfs(node.right, length, total)

        dfs(root, 0, 0)

        return self.maxSum
