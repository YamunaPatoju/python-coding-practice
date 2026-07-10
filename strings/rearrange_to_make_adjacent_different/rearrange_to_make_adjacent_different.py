class Solution:
    def canRearrange(self, s):

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        maxFreq = max(freq)

        return maxFreq <= (len(s) + 1) // 2
