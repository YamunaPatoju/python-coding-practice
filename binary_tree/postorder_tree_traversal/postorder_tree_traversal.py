class Solution:
    def postorder_recursive(self, root):
        result = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.data)

        dfs(root)
        return result

    def postorder_iterative(self, root):
        if root is None:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.data)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return result[::-1]
