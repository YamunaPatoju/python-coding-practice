# Median in a Row-wise Sorted Matrix

## Problem Statement

Given a row-wise sorted matrix with an odd number of rows and columns, find the median of all elements in the matrix.

The median is the middle element after sorting all elements.

## Example 1

Input:

```text
[
 [1, 3, 5],
 [2, 6, 9],
 [3, 6, 9]
]
```

Output:

```text
5
```

Explanation:

```text
Sorted elements:
[1, 2, 3, 3, 5, 6, 6, 9, 9]

Middle element = 5
```

## Example 2

Input:

```text
[
 [2, 4, 9],
 [3, 6, 7],
 [4, 7, 10]
]
```

Output:

```text
6
```

## Approach

I first collected all matrix elements into a single array.

Then I sorted the array and returned the middle element since the total number of elements is always odd.

