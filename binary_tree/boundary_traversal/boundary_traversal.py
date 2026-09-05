class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []

        ans = []

        def is_leaf(node):
            return node.left is None and node.right is None

        def left_boundary(node):
            while node:
                if not is_leaf(node):
                    ans.append(node.data)

                if node.left:
                    node = node.left
                else:
                    node = node.right

        def leaves(node):
            if not node:
                return

            if is_leaf(node):
                ans.append(node.data)
                return

            leaves(node.left)
            leaves(node.right)

        def right_boundary(node):
            temp = []

            while node:
                if not is_leaf(node):
                    temp.append(node.data)

                if node.right:
                    node = node.right
                else:
                    node = node.left

            ans.extend(temp[::-1])

        if is_leaf(root):
            return [root.data]

        ans.append(root.data)

        if root.left:
            left_boundary(root.left)

        leaves(root)

        if root.right:
            right_boundary(root.right)

        return ans
