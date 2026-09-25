class Solution:
    def kthSmallest(self, root, k):
        result = [None]

        def inorder(node):
            if node is None or result[0] is not None:
                return

            inorder(node.left)

            if result[0] is not None:
                return

            k[0] -= 1

            if k[0] == 0:
                result[0] = node.data
                return

            inorder(node.right)

        k = [k]
        inorder(root)

        if result[0] is None:
            return -1

        return result[0]
