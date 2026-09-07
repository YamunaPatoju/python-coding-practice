class Solution:
    def toSumTree(self, root):
        def solve(node):
            if not node:
                return 0

            old = node.data

            left_sum = solve(node.left)
            right_sum = solve(node.right)

            node.data = left_sum + right_sum

            return old + left_sum + right_sum

        solve(root)
        return root
