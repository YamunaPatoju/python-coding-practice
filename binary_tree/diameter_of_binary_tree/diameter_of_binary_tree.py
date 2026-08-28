class Solution:
    def diameter(self, root):
        self.ans = 0

        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            self.ans = max(self.ans, left + right)

            return 1 + max(left, right)

        height(root)
        return self.ans
      
