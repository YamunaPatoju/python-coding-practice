# Kth Smallest Element in a Matrix

## Problem Statement

Given an n × n matrix where each row and column is sorted in non-decreasing order, find the kth smallest element in the matrix.

## Example 1

Input:

```text
[
 [16, 28, 60, 64],
 [22, 41, 63, 91],
 [27, 50, 87, 93],
 [36, 78, 87, 94]
]

k = 3
```

Output:

```text
27
```

Explanation:

Sorted elements:

```text
[16, 22, 27, 28, 36, 41, 50, 60, 63, 64, 78, 87, 87, 91, 93, 94]
```

3rd smallest element = 27

## Example 2

Input:

```text
[
 [10, 20, 30, 40],
 [15, 25, 35, 45],
 [24, 29, 37, 48],
 [32, 33, 39, 50]
]

k = 7
```

Output:

```text
30
```

## Approach

I store all matrix elements in a single array.

Then I sort the array and return the element at index `k - 1`.

This is easy to understand and works correctly for all test cases.

