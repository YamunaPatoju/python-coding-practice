from collections import deque

class Solution:
    def topView(self, root):
        if root is None:
            return []

        queue = deque([(root, 0)])
        top = {}

        while queue:
            node, hd = queue.popleft()

            if hd not in top:
                top[hd] = node.data

            if node.left:
                queue.append((node.left, hd - 1))

            if node.right:
                queue.append((node.right, hd + 1))

        return [top[hd] for hd in sorted(top)]
