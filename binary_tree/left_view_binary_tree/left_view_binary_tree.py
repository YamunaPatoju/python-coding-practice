from collections import deque

class Solution:
    def leftView(self, root):
        if root is None:
            return []

        ans = []
        q = deque([root])

        while q:
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()

                # First node of every level
                if i == 0:
                    ans.append(node.data)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return ans
