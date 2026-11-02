class Solution:
    def smallestNumber(self, s, d):
        if s > 9 * d:
            return "-1"

        if s == 0:
            return "-1"

        digits = [0] * d
        s -= 1

        for i in range(d - 1, 0, -1):
            if s > 9:
                digits[i] = 9
                s -= 9
            else:
                digits[i] = s
                s = 0

        digits[0] = s + 1

        return ''.join(map(str, digits))
