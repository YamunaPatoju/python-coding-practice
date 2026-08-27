from collections import deque

class Solution:
    def reverseLevelOrder(self, root):
        if root is None:
            return []

        q = deque([root])
        result = []

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.data)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            result.insert(0, level)

        return [x for level in result for x in level]
