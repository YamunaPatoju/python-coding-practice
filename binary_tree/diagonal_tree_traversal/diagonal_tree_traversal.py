from collections import deque

class Solution:
    def diagonal(self, root):
        if root is None:
            return []

        result = []
        q = deque([root])

        while q:
            node = q.popleft()

            while node:
                result.append(node.data)

                if node.left:
                    q.append(node.left)

                node = node.right

        return result
