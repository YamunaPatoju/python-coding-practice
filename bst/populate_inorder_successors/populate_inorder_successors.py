class Solution:
    def populateNext(self, root):
        previous = [None]

        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            if previous[0]:
                previous[0].next = node

            previous[0] = node

            inorder(node.right)

        inorder(root)
