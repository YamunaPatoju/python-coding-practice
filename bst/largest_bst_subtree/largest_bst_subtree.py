class Solution:
    def largestBst(self, root):
        def solve(node):
            if node is None:
                return True, 0, float("inf"), float("-inf")

            left_bst, left_size, left_min, left_max = solve(node.left)
            right_bst, right_size, right_min, right_max = solve(node.right)

            if (
                left_bst
                and right_bst
                and left_max < node.data < right_min
            ):
                size = left_size + right_size + 1

                return (
                    True,
                    size,
                    min(left_min, node.data),
                    max(right_max, node.data)
                )

            return (
                False,
                max(left_size, right_size),
                0,
                0
            )

        _, size, _, _ = solve(root)

        return size
