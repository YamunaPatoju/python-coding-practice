class Solution:
    def minFlips(self, s):

        flip1 = 0
        flip2 = 0

        for i in range(len(s)):

            expected1 = '0' if i % 2 == 0 else '1'
            expected2 = '1' if i % 2 == 0 else '0'

            if s[i] != expected1:
                flip1 += 1

            if s[i] != expected2:
                flip2 += 1

        return min(flip1, flip2)
