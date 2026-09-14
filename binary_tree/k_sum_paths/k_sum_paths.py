class Solution:
    def printKPath(self, root, k):
        result = []
        path = []

        def dfs(node):
            if node is None:
                return

            path.append(node.data)

            dfs(node.left)
            dfs(node.right)

            total = 0

            for i in range(len(path) - 1, -1, -1):
                total += path[i]

                if total == k:
                    result.append(path[i:].copy())

            path.pop()

        dfs(root)
        return result
