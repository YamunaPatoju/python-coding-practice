class Solution:
    def minMovesToMakePalindrome(self, s):
        s = list(s)
        moves = 0

        while len(s) > 1:
            i = len(s) - 1

            while i > 0 and s[i] != s[0]:
                i -= 1

            if i == 0:
                moves += 1
                s[0], s[1] = s[1], s[0]
            else:
                while i < len(s) - 1:
                    s[i], s[i + 1] = s[i + 1], s[i]
                    moves += 1
                    i += 1

                s.pop()
                s.pop(0)

        return moves
