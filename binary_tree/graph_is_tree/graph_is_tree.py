from collections import deque


class Solution:
    def isTree(self, n, m, edges):
        if m != n - 1:
            return False

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        queue = deque([(0, -1)])
        visited[0] = True

        count = 0

        while queue:
            node, parent = queue.popleft()
            count += 1

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return False

        return count == n
