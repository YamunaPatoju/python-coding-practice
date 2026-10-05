# Fractional Knapsack

## Problem

Given two arrays `val[]` and `wt[]`, where:

* `val[i]` is the value of item `i`
* `wt[i]` is the weight of item `i`

and a knapsack capacity, find the maximum total value that can be obtained.

Unlike the 0/1 Knapsack problem, items can be broken into fractions.

Return the maximum value rounded to 6 decimal places.

## Approach

Use a **Greedy** approach.

For every item, calculate its **value-to-weight ratio**:

```text
value / weight
```

An item with a higher ratio gives more value for every unit of weight.

Therefore:

1. Calculate the value/weight ratio for every item.
2. Sort items by decreasing ratio.
3. Take the complete item if it fits.
4. If it does not fit, take the fraction that fits.
5. Stop when the knapsack becomes full.

## Algorithm

```text
Create a list containing:
    value / weight ratio
    value
    weight

Sort items by decreasing ratio.

For every item:
    If the complete item fits:
        take the complete item
        reduce capacity

    Otherwise:
        take the required fraction
        add proportional value
        stop
```

## Example 1

### Input

```text
val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50
```

Value/weight ratios:

```text
60 / 10 = 6
100 / 20 = 5
120 / 30 = 4
```

Take:

```text
10 kg → 60
20 kg → 100
20 kg of the 30 kg item → 80
```

Total:

```text
60 + 100 + 80 = 240
```

### Output

```text
240.000000
```

