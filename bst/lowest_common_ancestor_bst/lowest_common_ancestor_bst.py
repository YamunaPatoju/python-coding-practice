class Solution:
    def findLCA(self, root, n1, n2):
        while root:
            if n1.data < root.data and n2.data < root.data:
                root = root.left

            elif n1.data > root.data and n2.data > root.data:
                root = root.right

            else:
                return root

        return None
