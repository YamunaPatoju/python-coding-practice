# Minimum Cost to Cut a Board into Squares

## Problem

Given a board of dimensions `n × m`, divide it into `1 × 1` squares using vertical and horizontal cuts.

* `x[]` contains the costs of vertical cuts.
* `y[]` contains the costs of horizontal cuts.

The cost of a vertical cut is multiplied by the current number of horizontal segments. The cost of a horizontal cut is multiplied by the current number of vertical segments.

Find the minimum total cost required to cut the board into squares.

## Approach

Use a **Greedy** approach.

* Sort both cost arrays in descending order.
* Always choose the largest available cut cost first.
* Multiply each cut's cost by the number of segments in the opposite direction.
* Update the corresponding segment count after every cut.

## Algorithm

1. Sort `x` and `y` in descending order.
2. Initialize vertical and horizontal segment counts to `1`.
3. Compare the next available vertical and horizontal cut costs.
4. Choose the larger cost and calculate its total cost using the opposite-direction segment count.
5. Increase the corresponding segment count.
6. Process all remaining cuts.
7. Return the total cost.

## Example

### Input

```text
n = 4
m = 6
x = [2, 1, 3, 1, 4]
y = [4, 1, 2]
```

### Output

```text
42
```
