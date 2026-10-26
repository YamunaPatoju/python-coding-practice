# CHOCOLA — Chocolate Breaking

## Problem
Given an `m × n` chocolate bar and the costs of breaking along its vertical and horizontal lines, find the minimum total cost required to break it into individual squares.

Each break's cost is multiplied by the number of existing pieces in the perpendicular direction.

## Approach
Use a greedy approach by sorting both sets of costs in descending order. Always perform the most expensive available break first, because doing so while there are fewer pieces in the perpendicular direction minimizes the total cost.

- `vertical` tracks the number of vertical pieces.
- `horizontal` tracks the number of horizontal pieces.
- A vertical cut costs `x[i] * horizontal`.
- A horizontal cut costs `y[j] * vertical`.

## Algorithm
1. Read the number of test cases and skip the blank line.
2. Read `m`, `n`, and all vertical and horizontal cut costs.
3. Sort both cost lists in descending order.
4. Initialize the vertical and horizontal piece counts to `1`.
5. Compare the largest remaining costs:
   - If the vertical cost is larger, add its cost multiplied by the horizontal piece count and increase the vertical piece count.
   - Otherwise, add the horizontal cost multiplied by the vertical piece count and increase the horizontal piece count.
6. Process any remaining cuts.
7. Print the minimum total cost.

## Example

**Input:**
```text
1

6 4
2
1
3
1
4
4
1
2
```

**Output:**
```text
42
```


