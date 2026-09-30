class Solution:
    def isDeadEnd(self, root):
        def check(node, low, high):
            if node is None:
                return False

            # Leaf node
            if node.left is None and node.right is None:
                return low == high

            return (
                check(node.left, low, node.data - 1)
                or check(node.right, node.data + 1, high)
            )

        return check(root, 1, 10**5)
