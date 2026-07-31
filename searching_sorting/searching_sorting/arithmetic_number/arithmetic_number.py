class Solution:
    def inSequence(self, a, b, c):
        if a == b:
            return True

        if c == 0:
            return False

        diff = b - a

        if diff % c != 0:
            return False

        return diff // c >= 0
