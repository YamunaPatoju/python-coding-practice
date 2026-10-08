class Solution:
    def minMaxCandy(self, prices, k):
        prices.sort()

        n = len(prices)

        minimum = 0
        i = 0
        j = n - 1

        while i <= j:
            minimum += prices[i]
            i += 1
            j -= k

        maximum = 0
        i = 0
        j = n - 1

        while i <= j:
            maximum += prices[j]
            j -= 1
            i += k

        return [minimum, maximum]
