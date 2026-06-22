# Maximum Rectangle of 1's in a Binary Matrix

## Problem Statement

Given a binary matrix containing only 0s and 1s, find the area of the largest rectangle that contains only 1s.

## Example 1

Input:

```text
[
 [0,1,1,0],
 [1,1,1,1],
 [1,1,1,1],
 [1,1,0,0]
]
```

Output:

```text
8
```

Explanation:

```text
[1,1,1,1]
[1,1,1,1]
```

Area = 4 × 2 = 8

## Example 2

Input:

```text
[
 [0,1,1],
 [1,1,1],
 [0,1,1]
]
```

Output:

```text
6
```

Explanation:

```text
[1,1]
[1,1]
[1,1]
```

Area = 2 × 3 = 6

## Approach

For every row, I build a histogram.

- If the current cell is 1, increase the height.
- If the current cell is 0, reset the height to 0.

After updating heights for a row, I find the largest rectangle in the histogram using a stack.

The maximum area found across all rows is the answer.

