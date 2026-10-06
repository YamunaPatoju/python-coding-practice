class Solution:
    def chooseSwap(self, s):
        first = [-1] * 26

        for i, ch in enumerate(s):
            index = ord(ch) - ord('a')
            if first[index] == -1:
                first[index] = i

        for i in range(len(s)):
            current = ord(s[i]) - ord('a')

            for smaller in range(current):
                if first[smaller] != -1 and first[smaller] > i:
                    a = chr(current + ord('a'))
                    b = chr(smaller + ord('a'))

                    result = list(s)

                    for j in range(len(result)):
                        if result[j] == a:
                            result[j] = b
                        elif result[j] == b:
                            result[j] = a

                    return ''.join(result)

        return s
