class Solution:
    def countPairs(self, root1, root2, x):
        values = set()

        def inorder1(node):
            if node is None:
                return

            inorder1(node.left)
            values.add(node.data)
            inorder1(node.right)

        inorder1(root1)

        count = 0

        def inorder2(node):
            nonlocal count

            if node is None:
                return

            inorder2(node.left)

            if x - node.data in values:
                count += 1

            inorder2(node.right)

        inorder2(root2)

        return count
