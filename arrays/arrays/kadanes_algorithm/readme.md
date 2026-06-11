# Kadane's Algorithm

## Problem Statement

Given an integer array `arr[]`, find the maximum sum of a contiguous subarray.

A subarray is a continuous part of an array.

## Example 1

**Input:**

[2, 3, -8, 7, -1, 2, 3]

**Output:**

11

**Explanation:**

The subarray [7, -1, 2, 3] has the maximum sum 11.

## Example 2

**Input:**

[-2, -4]

**Output:**

-2

**Explanation:**

The subarray [-2] has the maximum sum.

## Example 3

**Input:**

[5, 4, 1, 7, 8]

**Output:**

25

**Explanation:**

The entire array forms the maximum sum subarray.

## Approach

Kadane's Algorithm is used to find the maximum subarray sum in a single traversal.

1. Initialize:

   * `current_sum` with the first element.
   * `max_sum` with the first element.
2. Traverse the array from the second element.
3. For each element:

   * Either start a new subarray from the current element.
   * Or extend the existing subarray.
4. Update the maximum sum found so far.
5. Return the maximum sum.

