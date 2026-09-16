from collections import defaultdict

class Solution:
    def printAllDups(self, root):
        count = defaultdict(int)
        result = []

        def dfs(node):
            if node is None:
                return "#"

            left = dfs(node.left)
            right = dfs(node.right)

            key = str(node.data) + "," + left + "," + right

            count[key] += 1

            if count[key] == 2:
                result.append(node)

            return key

        dfs(root)
        return result
