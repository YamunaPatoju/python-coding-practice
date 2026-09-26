class Solution:
    def findMedian(self, root):
        values = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            values.append(node.data)
            inorder(node.right)

        inorder(root)

        n = len(values)

        if n % 2 == 1:
            return values[n // 2]

        return values[(n // 2) - 1]
