from collections import deque

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        q = deque([root])
        result = []

        while q:
            node = q.popleft()
            result.append(node.data)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return result
