class Solution:
    def getCount(self, root, l, h):
        if root is None:
            return 0

        if root.data < l:
            return self.getCount(root.right, l, h)

        if root.data > h:
            return self.getCount(root.left, l, h)

        return (
            1
            + self.getCount(root.left, l, h)
            + self.getCount(root.right, l, h)
        )
