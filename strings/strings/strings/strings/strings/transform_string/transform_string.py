class Solution:
    def transform(self, s1, s2):

        if len(s1) != len(s2):
            return -1

        if sorted(s1) != sorted(s2):
            return -1

        i = len(s1) - 1
        j = len(s2) - 1
        count = 0

        while i >= 0:

            if s1[i] == s2[j]:
                i -= 1
                j -= 1
            else:
                count += 1
                i -= 1

        return count
