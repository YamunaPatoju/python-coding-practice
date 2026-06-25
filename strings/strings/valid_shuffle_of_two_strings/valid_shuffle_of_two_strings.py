class Solution:
    def checkShuffle(self, first, second, result):

        if len(first) + len(second) != len(result):
            return False

        i = j = k = 0

        while k < len(result):

            if i < len(first) and first[i] == result[k]:
                i += 1

            elif j < len(second) and second[j] == result[k]:
                j += 1

            else:
                return False

            k += 1

        return i == len(first) and j == len(second)
