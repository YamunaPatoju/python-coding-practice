class Solution:
    def check(self, root):
        level = -1

        def dfs(node, depth):
            nonlocal level

            if node is None:
                return True

            if node.left is None and node.right is None:
                if level == -1:
                    level = depth
                    return True
                return level == depth

            return dfs(node.left, depth + 1) and dfs(node.right, depth + 1)

        return dfs(root, 0)
