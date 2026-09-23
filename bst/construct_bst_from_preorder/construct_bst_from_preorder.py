class Solution:
    def bstFromPreorder(self, preorder):
        index = [0]

        def build(min_value, max_value):
            if index[0] >= len(preorder):
                return None

            value = preorder[index[0]]

            if value < min_value or value > max_value:
                return None

            index[0] += 1

            node = TreeNode(value)

            node.left = build(min_value, value - 1)
            node.right = build(value + 1, max_value)

            return node

        return build(float("-inf"), float("inf"))
