# Maximum Difference Between Pair in a Matrix

## Problem Statement

Given an `n × n` matrix, find the maximum value of:

mat[c][d] - mat[a][b]

such that:

```text
c > a
d > b
```

This means the second element must be located strictly below and to the right of the first element.

## Example

Input:

```text
[
 [1, 2, -1, -4, -20],
 [-8, -3, 4, 2, 1],
 [3, 8, 6, 1, 3],
 [-4, -1, 1, 7, -6],
 [0, -4, 10, -5, 1]
]
```

Output:

```text
18
```

Explanation:

```text
10 - (-8) = 18
```

This is the maximum possible difference where the second element is to the bottom-right of the first element.

## Approach

Instead of checking every possible pair, I create a helper matrix called `maxArr`.

`maxArr[i][j]` stores the maximum value present in the submatrix from `(i, j)` to the bottom-right corner.

Then for every cell, I calculate:

```text
maxArr[i + 1][j + 1] - mat[i][j]
```

and keep track of the maximum difference.

This reduces the time complexity significantly.

