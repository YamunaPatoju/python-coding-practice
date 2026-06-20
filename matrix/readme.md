# Spiral Traversal of Matrix

## Problem Statement

Given a matrix, traverse all its elements in spiral order and return the result.

The traversal starts from the top row, then moves right, down, left, and up repeatedly until all elements are visited.

## Example 1

Input:

```text
[
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14, 15, 16]
]
```

Output:

```text
[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
```

## Example 2

Input:

```text
[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
```

Output:

```text
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```

## Approach

I used four pointers:

- top
- bottom
- left
- right

These pointers represent the current boundaries of the matrix.

At each step:

1. Traverse from left to right.
2. Traverse from top to bottom.
3. Traverse from right to left.
4. Traverse from bottom to top.

After each traversal, update the boundaries and continue until all elements are visited.

