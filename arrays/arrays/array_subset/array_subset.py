class Solution:
    def isSubset(self, a, b):
        freq = {}

        for num in a:
            freq[num] = freq.get(num, 0) + 1

        for num in b:
            if num not in freq or freq[num] == 0:
                return False

            freq[num] -= 1

        return True
