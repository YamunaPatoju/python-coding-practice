# Sort a Matrix

## Problem Statement

Given an n × n matrix, sort all its elements in non-decreasing order and return the sorted matrix.

## Example 1

Input:

```text
[
 [10, 20, 30, 40],
 [15, 25, 35, 45],
 [27, 29, 37, 48],
 [32, 33, 39, 50]
]
```

Output:

```text
[
 [10, 15, 20, 25],
 [27, 29, 30, 32],
 [33, 35, 37, 39],
 [40, 45, 48, 50]
]
```

## Example 2

Input:

```text
[
 [1, 5, 3],
 [2, 8, 7],
 [4, 6, 9]
]
```

Output:

```text
[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
```

## Approach

I first store all matrix elements in a single array.

Then I sort the array.

After sorting, I place the elements back into the matrix row by row.

This gives a matrix where all elements are arranged in non-decreasing order.
