# Next Permutation

## Problem Statement

Given an array representing a permutation, rearrange it into the next lexicographically greater permutation.

If no greater permutation exists, rearrange it into the smallest possible order (ascending).

## Example 1

**Input:**

```text
arr = [2, 4, 1, 7, 5, 0]
```

**Output:**

```text
[2, 4, 5, 0, 1, 7]
```

## Example 2

**Input:**

```text
arr = [3, 2, 1]
```

**Output:**

```text
[1, 2, 3]
```

## Example 3

**Input:**

```text
arr = [3, 4, 2, 5, 1]
```

**Output:**

```text
[3, 4, 5, 1, 2]
```

## Approach

- Traverse from right to left to find the first decreasing element.
- Find the smallest element greater than it on the right.
- Swap the two elements.
- Reverse the remaining suffix to get the next smallest arrangement.
