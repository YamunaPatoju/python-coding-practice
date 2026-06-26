class Solution:
    def powerSet(self, s):

        result = []

        def solve(index, curr):
            if index == len(s):
                result.append(curr)
                return
            solve(index + 1, curr + s[index])
            solve(index + 1, curr)

        solve(0, "")

        result.sort()

        return result
