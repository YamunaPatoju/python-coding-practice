# Max Value Permutation

## Problem
Given an array of integers, rearrange its elements to maximize the sum of `arr[i] * i`, where `0 <= i < n`. Return the result modulo `10^9 + 7`.

## Approach
- Sort the array in ascending order.
- Multiply each element by its index.
- Add all products while applying the modulo.

## Algorithm
1. Sort the array in ascending order.
2. Initialize `total = 0`.
3. Traverse the array and add `arr[i] * i` to `total`.
4. Apply modulo `10^9 + 7` during each addition.
5. Return `total`.

## Example
**Input:** `arr = [5, 3, 2, 4, 1]`

**Sorted array:** `[1, 2, 3, 4, 5]`

**Calculation:** `1*0 + 2*1 + 3*2 + 4*3 + 5*4 = 40`

**Output:** `40`


