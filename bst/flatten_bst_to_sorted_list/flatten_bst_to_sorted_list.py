class Solution:
    def flattenBST(self, root):
        values = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            values.append(node)
            inorder(node.right)

        inorder(root)

        for i in range(len(values)):
            values[i].left = None

            if i + 1 < len(values):
                values[i].right = values[i + 1]
            else:
                values[i].right = None

        return values[0] if values else None
