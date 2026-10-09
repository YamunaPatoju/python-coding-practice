class Solution:
    def minCost(self, n, m, x, y):
        x.sort(reverse=True)
        y.sort(reverse=True)

        vertical_segments = 1
        horizontal_segments = 1

        i = 0
        j = 0
        total_cost = 0

        while i < len(x) and j < len(y):
            if x[i] >= y[j]:
                total_cost += x[i] * horizontal_segments
                vertical_segments += 1
                i += 1
            else:
                total_cost += y[j] * vertical_segments
                horizontal_segments += 1
                j += 1

        while i < len(x):
            total_cost += x[i] * horizontal_segments
            vertical_segments += 1
            i += 1

        while j < len(y):
            total_cost += y[j] * vertical_segments
            horizontal_segments += 1
            j += 1

        return total_cost
