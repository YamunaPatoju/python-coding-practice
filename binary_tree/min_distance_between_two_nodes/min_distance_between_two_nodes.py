class Solution:
    def findDist(self, root, a, b):
        def lca(node):
            if node is None:
                return None

            if node.data == a or node.data == b:
                return node

            left = lca(node.left)
            right = lca(node.right)

            if left and right:
                return node

            return left if left else right

        def distance(node, target):
            if node is None:
                return -1

            if node.data == target:
                return 0

            left = distance(node.left, target)

            if left != -1:
                return left + 1

            right = distance(node.right, target)

            if right != -1:
                return right + 1

            return -1

        ancestor = lca(root)

        return distance(ancestor, a) + distance(ancestor, b)
