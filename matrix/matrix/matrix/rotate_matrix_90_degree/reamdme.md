# Rotate Matrix by 90 Degrees Clockwise

## Problem Statement

Given an N × N matrix, rotate it by 90 degrees in the clockwise direction.

## Example

Input:

```text
1  2  3  4
5  6  7  8
9 10 11 12
13 14 15 16
```

Output:

```text
13  9  5  1
14 10  6  2
15 11  7  3
16 12  8  4
```

## Approach

I create a new matrix of the same size.
Using nested loops, each element is placed in its new position after a 90-degree clockwise rotation.
Finally, the rotated matrix is copied back to the original matrix.

Finally, the rotated matrix is copied back to the original matrix.

