class Solution:
    def minimumNumberOfSwaps(self, s):

        pos = []

        for i in range(len(s)):
            if s[i] == '[':
                pos.append(i)

        s = list(s)

        p = 0
        count = 0
        swaps = 0

        for i in range(len(s)):

            if s[i] == '[':
                count += 1
                p += 1
            else:
                count -= 1

            if count < 0:
                swaps += pos[p] - i

                s[i], s[pos[p]] = s[pos[p]], s[i]

                p += 1
                count = 1

        return swaps
