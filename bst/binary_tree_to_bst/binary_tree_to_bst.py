class Solution:
    def binaryTreeToBST(self, root):
        values = []

        def inorder_collect(node):
            if node is None:
                return

            inorder_collect(node.left)
            values.append(node.data)
            inorder_collect(node.right)

        inorder_collect(root)

        values.sort()

        index = [0]

        def inorder_update(node):
            if node is None:
                return

            inorder_update(node.left)

            node.data = values[index[0]]
            index[0] += 1

            inorder_update(node.right)

        inorder_update(root)

        return root
