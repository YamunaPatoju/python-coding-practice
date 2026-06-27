class Solution:
    def findPermutation(self, s):

        result = []
        chars = sorted(s)
        used = [False] * len(chars)

        def backtrack(path):

            if len(path) == len(chars):
                result.append("".join(path))
                return

            for i in range(len(chars)):

                if used[i]:
                    continue
                if i > 0 and chars[i] == chars[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(chars[i])

                backtrack(path)

                path.pop()
                used[i] = False

        backtrack([])

        return result
