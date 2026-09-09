class Solution:
    def isSumTree(self, root):

        def solve(node):
            if node is None:
                return True, 0

            if node.left is None and node.right is None:
                return True, node.data

            left_ok, left_sum = solve(node.left)
            right_ok, right_sum = solve(node.right)

            current_ok = (
                left_ok and
                right_ok and
                node.data == left_sum + right_sum
            )

            return current_ok, node.data + left_sum + right_sum

        result, _ = solve(root)
        return result
