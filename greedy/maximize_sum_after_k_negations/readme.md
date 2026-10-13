# Maximize Sum After K Negations

## Problem
Given an integer array `arr` and an integer `k`, perform exactly `k` sign-change operations to maximize the array sum.

## Approach
- Sort the array in ascending order.
- Change negative elements to positive, starting with the smallest values, while operations remain.
- If operations remain odd, flip the element with the smallest absolute value.

## Algorithm
1. Sort the array.
2. Traverse the array and negate negative elements while `k > 0`.
3. If `k` is odd after processing negative elements, sort the array again and negate its smallest element.
4. Return the sum of the array.
