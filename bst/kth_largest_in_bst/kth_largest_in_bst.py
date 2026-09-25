class Solution:
    def kthLargest(self, root, k):
        result = [None]

        def reverse_inorder(node):
            if node is None or result[0] is not None:
                return

            reverse_inorder(node.right)

            if result[0] is not None:
                return

            k[0] -= 1

            if k[0] == 0:
                result[0] = node.data
                return

            reverse_inorder(node.left)

        k = [k]
        reverse_inorder(root)

        return result[0]
