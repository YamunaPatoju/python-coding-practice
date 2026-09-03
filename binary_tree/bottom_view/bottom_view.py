from collections import deque

class Solution:
    def bottomView(self, root):
        if root is None:
            return []

        queue = deque([(root, 0)])
        bottom = {}

        while queue:
            node, hd = queue.popleft()

            # Overwrite so the latter node in level order is kept
            bottom[hd] = node.data

            if node.left:
                queue.append((node.left, hd - 1))

            if node.right:
                queue.append((node.right, hd + 1))

        return [bottom[hd] for hd in sorted(bottom)]
