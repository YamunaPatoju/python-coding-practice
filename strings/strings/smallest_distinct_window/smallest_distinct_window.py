class Solution:
    def findSubString(self, s):

        distinct = len(set(s))
        freq = {}

        left = 0
        count = 0
        ans = len(s)

        for right in range(len(s)):

            freq[s[right]] = freq.get(s[right], 0) + 1

            if freq[s[right]] == 1:
                count += 1

            while count == distinct:

                ans = min(ans, right - left + 1)

                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    count -= 1

                left += 1

        return ans
