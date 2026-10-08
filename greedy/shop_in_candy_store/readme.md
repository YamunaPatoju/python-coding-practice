# Shop in Candy Store

## Problem

Given the prices of different types of candies, for every candy bought, we can get up to `k` other different candies for free.

Find the **minimum** and **maximum** amount of money needed to buy all the candies.

In both cases, the maximum possible number of free candies must be taken.

## Approach

Use a **Greedy** approach after sorting the prices.

### Minimum Cost

* Sort the prices in ascending order.
* Buy the cheapest available candy.
* Take the `k` most expensive remaining candies for free.
* Repeat until all candies are covered.

### Maximum Cost

* Sort the prices in ascending order.
* Buy the most expensive available candy.
* Take the `k` cheapest remaining candies for free.
* Repeat until all candies are covered.

## Algorithm

1. Sort the candy prices.
2. For minimum cost:

   * Start from the cheapest candy.
   * Add its price to the cost.
   * Skip `k` candies from the expensive end as free.
3. For maximum cost:

   * Start from the most expensive candy.
   * Add its price to the cost.
   * Skip `k` candies from the cheap end as free.
4. Return the minimum and maximum costs.

## Example

### Input

```text
prices = [3, 2, 1, 4]
k = 2
```

Sorted prices:

```text
[1, 2, 3, 4]
```

### Minimum Cost

Buy:

```text
1 + 2 = 3
```

The remaining expensive candies are taken for free.

Minimum cost = `3`

### Maximum Cost

Buy:

```text
4 + 3 = 7
```

The remaining cheap candies are taken for free.

Maximum cost = `7`

### Output

```text
[3, 7]
```

