# Minimum Size Subarray Sum

## Problem Statement

Given an array of positive integers `nums` and a positive integer `target`, find the minimum length of a contiguous subarray whose sum is greater than or equal to `target`.

If no such subarray exists, return `0`.

## Example 1

Input:

```text
target = 7
nums = [2, 3, 1, 2, 4, 3]
```

Output:

```text
2
```
## Example 2

Input:

```text
target = 4
nums = [1, 4, 4]
```

Output:

```text
1
```
## Approach

I used the Sliding Window technique.

- Expand the window by moving the right pointer.
- Keep adding elements to the current sum.
- When the sum becomes greater than or equal to the target, shrink the window from the left.
- Update the minimum length whenever a valid subarray is found.

This helps find the answer efficiently in a single traversal.

