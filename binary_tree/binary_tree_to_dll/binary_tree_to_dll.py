class Solution:
    def treeToDLL(self, root):
        self.prev = None
        self.head = None

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev is None:
                self.head = node
            else:
                self.prev.right = node
                node.left = self.prev

            self.prev = node

            inorder(node.right)

        inorder(root)
        return self.head
