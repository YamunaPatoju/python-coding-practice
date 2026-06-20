# Search a 2D Matrix

## Problem Statement

Given a matrix where:

- Each row is sorted in non-decreasing order.
- The first element of each row is greater than the last element of the previous row.

Determine whether a given target value exists in the matrix.

## Example 1

Input:

```text
matrix = [
 [1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]
]

target = 3
```

Output:

```text
True
```

## Example 2

Input:

```text
matrix = [
 [1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]
]

target = 13
```

Output:

```text
False
```

## Approach

Since the matrix is sorted and each row starts with a value greater than the previous row's last value, we can treat the entire matrix as a single sorted array.

Using Binary Search:

1. Set left and right pointers.
2. Find the middle element.
3. Convert the middle index into row and column.
4. Compare with target.
5. Move left or right accordingly.

This gives an efficient solution.

