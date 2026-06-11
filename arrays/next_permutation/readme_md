# Next Permutation

## Problem Statement

Given an array of integers, find the next lexicographically greater permutation of the array.

If no greater permutation exists, rearrange the array into the lowest possible order (ascending order).

The modification must be done in-place using constant extra memory.

## Example 1

**Input:**

[1, 2, 3]

**Output:**

[1, 3, 2]

## Example 2

**Input:**

[3, 2, 1]

**Output:**

[1, 2, 3]

## Example 3

**Input:**

[1, 1, 5]

**Output:**

[1, 5, 1]

## Approach

1. Traverse from right to left and find the first element that is smaller than its next element.
2. Find the smallest element greater than it on the right side.
3. Swap both elements.
4. Reverse the remaining suffix to get the next smallest lexicographical order.

## Algorithm

1. Find index `i` such that:

   nums[i] < nums[i + 1]

2. Find index `j` from the end such that:

   nums[j] > nums[i]

3. Swap nums[i] and nums[j].

4. Reverse the subarray from `i + 1` to the end.

