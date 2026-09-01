from collections import deque

class Solution:
    def rightView(self, root):
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # Last node of each level
                if i == level_size - 1:
                    result.append(node.data)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result
