# Largest Sum Contiguous Subarray

## Problem Statement

Given an array containing both positive and negative integers, find the contiguous subarray with the largest sum and return that sum.

## Example

**Input:**

[-2, -3, 4, -1, -2, 1, 5, -3]

**Output:**

7

## Explanation

The subarray:

[4, -1, -2, 1, 5]

has the largest sum:

4 + (-1) + (-2) + 1 + 5 = 7

## Approach

Use Kadane's Algorithm.

1. Initialize current sum and maximum sum with the first element.
2. For each element:

   * Either start a new subarray from the current element.
   * Or extend the existing subarray.
3. Update the maximum sum whenever a larger sum is found.
4. Return the maximum sum.

  
