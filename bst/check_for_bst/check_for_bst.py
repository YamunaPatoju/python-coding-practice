class Solution:
    def isBST(self, root):
        def check(node, low, high):
            if node is None:
                return True

            if node.data <= low or node.data >= high:
                return False

            return (
                check(node.left, low, node.data)
                and check(node.right, node.data, high)
            )

        return check(root, float("-inf"), float("inf"))
