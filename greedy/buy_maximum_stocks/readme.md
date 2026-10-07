# Buy Maximum Stocks

## Problem

Given the stock price for each day, a customer can buy at most `i` stocks on the `i`th day.

The customer initially has `k` amount of money.

Find the maximum number of stocks the customer can buy.

## Approach

Use a **Greedy** approach.

* Store each day's stock price and its maximum stock limit.
* Sort the days by stock price.
* Buy stocks from the cheapest day first.
* On each day, buy as many stocks as possible without exceeding the available money or that day's limit.

## Algorithm

1. Create pairs of `(price, maximum_stocks)` for every day.
2. Sort the pairs by price.
3. For each day:

   * Calculate how many stocks can be bought with the remaining money.
   * Limit the purchase to the maximum stocks allowed on that day.
   * Update the remaining money and total stock count.
4. Return the total number of stocks purchased.

## Example

### Input

```text
k = 46
price = [11, 13, 9, 4]
```

### Output

```text
7
```

