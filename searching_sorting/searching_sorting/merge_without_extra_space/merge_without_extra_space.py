class Solution:
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)

        gap = (n + m + 1) // 2

        while gap > 0:
            i = 0
            j = gap

            while j < n + m:
                if i < n:
                    x = a
                    xi = i
                else:
                    x = b
                    xi = i - n

                if j < n:
                    y = a
                    yj = j
                else:
                    y = b
                    yj = j - n

                if x[xi] > y[yj]:
                    x[xi], y[yj] = y[yj], x[xi]

                i += 1
                j += 1

            if gap == 1:
                break
            gap = (gap + 1) // 2
