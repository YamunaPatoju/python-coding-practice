class Solution:
    def isIsomorphic(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.data != root2.data:
            return False

        without_swap = (
            self.isIsomorphic(root1.left, root2.left) and
            self.isIsomorphic(root1.right, root2.right)
        )

        with_swap = (
            self.isIsomorphic(root1.left, root2.right) and
            self.isIsomorphic(root1.right, root2.left)
        )

        return without_swap or with_swap
