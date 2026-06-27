class Solution:
    def maxSubStr(self, s):

        count0 = 0
        count1 = 0
        ans = 0

        for ch in s:

            if ch == '0':
                count0 += 1
            else:
                count1 += 1

            if count0 == count1:
                ans += 1

        if count0 != count1:
            return -1

        return ans
