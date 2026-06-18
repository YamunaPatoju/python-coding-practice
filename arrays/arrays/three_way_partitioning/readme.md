# Three Way Partitioning

## Problem Statement

Given an array and two values `a` and `b`, partition the array into three parts:

1. Elements smaller than `a`
2. Elements between `a` and `b` (inclusive)
3. Elements greater than `b`

The order of elements within each group does not matter.

## Example 1

Input:

```text
arr = [1, 2, 3, 3, 4]
a = 1
b = 2
```

Output:

```text
[1, 2, 3, 3, 4]
```

## Example 2

Input:

```text
arr = [1, 4, 3, 6, 2, 1]
a = 1
b = 3
```

Output:

```text
[1, 1, 3, 2, 4, 6]
```

## Approach

I used the Dutch National Flag Algorithm with three pointers:

- `low` → tracks elements smaller than `a`
- `mid` → current element being processed
- `high` → tracks elements greater than `b`

This partitions the array in a single traversal.

