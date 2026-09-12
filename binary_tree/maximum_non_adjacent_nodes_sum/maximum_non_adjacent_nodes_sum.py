class Solution:
    def getMaxSum(self, root):
        def dfs(node):
            if node is None:
                return (0, 0)

            left_include, left_exclude = dfs(node.left)
            right_include, right_exclude = dfs(node.right)

            include = node.data + left_exclude + right_exclude

            exclude = max(left_include, left_exclude) + \
                      max(right_include, right_exclude)

            return (include, exclude)

        include, exclude = dfs(root)

        return max(include, exclude)
