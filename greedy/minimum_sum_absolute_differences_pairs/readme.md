# Minimum Sum of Absolute Differences of Pairs

## Problem
Given two arrays `a` and `b` of equal length, pair their elements to minimize the sum of absolute differences between the pairs.

## Approach
- Sort both arrays in ascending order.
- Pair elements at the same index.
- Calculate and add the absolute differences of the corresponding elements.

## Algorithm
1. Sort array `a`.
2. Sort array `b`.
3. Initialize `total = 0`.
4. Traverse both arrays and add `abs(a[i] - b[i])` to `total`.
5. Return `total`.

## Example
**Input:** `a = [4, 1, 8, 7]`, `b = [2, 3, 6, 5]`

**Sorted arrays:** `a = [1, 4, 7, 8]`, `b = [2, 3, 5, 6]`

**Calculation:** `|1-2| + |4-3| + |7-5| + |8-6| = 6`

**Output:** `6`
