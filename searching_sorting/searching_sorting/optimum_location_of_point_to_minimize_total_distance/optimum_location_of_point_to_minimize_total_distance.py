import math

class Solution:
    def findOptimumCost(self, L, n, points):
        a, b, c = L

        def dist(x, y):
            total = 0
            for px, py in points:
                total += math.sqrt((x - px) ** 2 + (y - py) ** 2)
            return total

        def f(x):
            if b != 0:
                y = (-c - a * x) / b
                return dist(x, y)
            else:
                x = -c / a
                return dist(x, 0)

        left, right = -100000.0, 100000.0

        while right - left > 1e-7:
            m1 = left + (right - left) / 3
            m2 = right - (right - left) / 3

            if f(m1) < f(m2):
                right = m2
            else:
                left = m1

        return round(f((left + right) / 2), 2)
