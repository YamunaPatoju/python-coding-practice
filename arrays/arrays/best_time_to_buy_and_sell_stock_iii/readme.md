# Best Time to Buy and Sell Stock III

## Problem Statement

You are given an array where `prices[i]` represents the stock price on day `i`.

You can perform at most **two transactions**.

A transaction means:

* Buy one stock.
* Sell that stock.

You must sell before buying again.

Return the maximum profit possible.

## Example 1

**Input:**

[3,3,5,0,0,3,1,4]

**Output:**

6

**Explanation:**

Transaction 1:

Buy at 0

Sell at 3

Profit = 3

Transaction 2:

Buy at 1

Sell at 4

Profit = 3

Total Profit = 6

## Example 2

**Input:**

[1,2,3,4,5]

**Output:**

4

## Example 3

**Input:**

[7,6,4,3,1]

**Output:**

0

## My Approach

Since we can make at most two transactions:

* First, calculate the maximum profit that can be earned from the left side of the array.
* Then calculate the maximum profit that can be earned from the right side.
* Combine both profits at every index.
* The maximum combined value is the answer.

I use two arrays:

* `left[i]` → Maximum profit from day 0 to day i.
* `right[i]` → Maximum profit from day i to the last day.

Finally, add both values and find the maximum profit.
