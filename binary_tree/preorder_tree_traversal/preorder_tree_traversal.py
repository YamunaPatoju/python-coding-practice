class Solution:
    def preorder_recursive(self, root):
        result = []

        def dfs(node):
            if node is None:
                return
            result.append(node.data)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result

    def preorder_iterative(self, root):
        if root is None:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.data)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result
