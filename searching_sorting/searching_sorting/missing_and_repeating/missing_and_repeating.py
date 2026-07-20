class Solution:
    def findTwoElement(self, arr):
        n = len(arr)

        xor = 0
        for num in arr:
            xor ^= num

        for i in range(1, n + 1):
            xor ^= i

        set_bit = xor & -xor

        x = 0
        y = 0

        for num in arr:
            if num & set_bit:
                x ^= num
            else:
                y ^= num

        for i in range(1, n + 1):
            if i & set_bit:
                x ^= i
            else:
                y ^= i

        if arr.count(x) == 2:
            return [x, y]
        else:
            return [y, x]
