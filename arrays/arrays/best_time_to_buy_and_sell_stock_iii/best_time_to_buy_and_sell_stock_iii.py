class Solution:
    def maxProfit(self, prices):
        n = len(prices)

        left = [0] * n
        right = [0] * n

        min_price = prices[0]

        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left[i] = max(left[i - 1], prices[i] - min_price)

        max_price = prices[-1]

        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right[i] = max(right[i + 1], max_price - prices[i])

        profit = 0

        for i in range(n):
            profit = max(profit, left[i] + right[i])

        return profit
