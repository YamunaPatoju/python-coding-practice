class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        items = []

        for i in range(len(val)):
            ratio = val[i] / wt[i]
            items.append((ratio, val[i], wt[i]))

        items.sort(reverse=True)

        total_value = 0.0

        for ratio, value, weight in items:
            if capacity >= weight:
                total_value += value
                capacity -= weight
            else:
                total_value += ratio * capacity
                break

        return round(total_value, 6)
