from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        count = [0] * 26
        q = deque()
        result = []

        for ch in s:
            count[ord(ch) - ord('a')] += 1
            q.append(ch)

            while q and count[ord(q[0]) - ord('a')] > 1:
                q.popleft()

            if q:
                result.append(q[0])
            else:
                result.append('#')

        return ''.join(result)
