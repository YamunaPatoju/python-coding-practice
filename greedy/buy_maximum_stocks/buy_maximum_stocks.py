class Solution:
    def buyMaximumProducts(self, k, price):
        stocks = []

        for i in range(len(price)):
            day = i + 1
            stocks.append((price[i], day))

        stocks.sort()

        count = 0

        for price_per_stock, max_stocks in stocks:
            can_buy = min(max_stocks, k // price_per_stock)

            count += can_buy
            k -= can_buy * price_per_stock

            if k == 0:
                break

        return count
