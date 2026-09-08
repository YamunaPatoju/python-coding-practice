class Solution:
    def buildTree(self, inorder, preorder):
        pos = {}

        for i in range(len(inorder)):
            pos[inorder[i]] = i

        preIndex = 0

        def build(left, right):
            nonlocal preIndex

            if left > right:
                return None

            root_value = preorder[preIndex]
            preIndex += 1

            root = Node(root_value)

            mid = pos[root_value]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
