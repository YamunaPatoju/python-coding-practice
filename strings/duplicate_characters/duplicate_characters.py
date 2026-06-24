class Solution:
    def printDuplicates(self, s):
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        result = []

        for ch in freq:
            if freq[ch] > 1:
                result.append([ch, freq[ch]])

        return result
