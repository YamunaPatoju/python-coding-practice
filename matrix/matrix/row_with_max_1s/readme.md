# Row with Maximum 1s

## Problem Statement

Given a binary matrix where each row is sorted, find the index of the first row that contains the maximum number of 1s.

If no row contains a 1, return -1.

## Example 1

Input:

```text
[
 [0,1,1,1],
 [0,0,1,1],
 [1,1,1,1],
 [0,0,0,0]
]
```

Output:

```text
2
```

Explanation:

Row 2 contains 4 ones, which is the maximum.

## Example 2

Input:

```text
[
 [0,0],
 [1,1]
]
```

Output:

```text
1
```

## Example 3

Input:

```text
[
 [0,0],
 [0,0]
]
```

Output:

```text
-1
```

## Approach

I traverse each row and count the number of 1s.

If the current row has more 1s than the previous maximum, I update:

- Maximum count of 1s
- Row index

At the end, I return the index of the row having the maximum number of 1s.
