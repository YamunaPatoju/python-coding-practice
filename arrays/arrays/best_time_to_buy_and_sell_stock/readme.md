# Best Time to Buy and Sell Stock

## Problem Statement

You are given an array where each element represents the stock price on a particular day.

Find the maximum profit that can be earned by buying the stock on one day and selling it on a later day.

If no profit can be made, return 0.

## Example 1

**Input:**

[7, 1, 5, 3, 6, 4]

**Output:**

5

**Explanation:**

Buy at price 1 and sell at price 6.

Profit = 6 - 1 = 5

## Example 2

**Input:**

[7, 6, 4, 3, 1]

**Output:**

0

**Explanation:**

Prices keep decreasing, so no profit can be made.

## My Approach

I keep track of the minimum stock price seen so far.

For every price:

* Calculate the profit if I sell on that day.
* Update the maximum profit if it is greater.
* Update the minimum price whenever a smaller price is found.

This allows finding the answer in a single traversal.

