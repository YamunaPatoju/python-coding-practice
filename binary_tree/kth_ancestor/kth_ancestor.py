class Solution:
    def kthAncestor(self, root, k, node):
        result = [-1]

        def dfs(current):
            if current is None:
                return False

            if current.data == node:
                return True

            left = dfs(current.left)
            right = dfs(current.right)

            if left or right:
                k[0] -= 1

                if k[0] == 0:
                    result[0] = current.data
                    return False

                return True

            return False

        k = [k]
        dfs(root)

        return result[0]
