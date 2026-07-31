class Solution:
    def findNum(self, n):
        def trailingZeros(x):
            count = 0
            while x:
                x //= 5
                count += x
            return count

        low = 1
        high = 5 * n

        while low < high:
            mid = (low + high) // 2

            if trailingZeros(mid) >= n:
                high = mid
            else:
                low = mid + 1

        return low
