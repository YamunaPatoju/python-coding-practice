# Maximum Sum of Absolute Difference of Any Permutation

## Problem
Given an array, rearrange its elements to maximize the sum of absolute differences between consecutive elements, including the difference between the last and first elements.

## Approach
- Sort the array in ascending order.
- Build a sequence by alternating between the smallest and largest remaining elements.
- Calculate the absolute differences between consecutive elements.
- Add the absolute difference between the last and first elements.

## Algorithm
1. Sort the array.
2. Use two pointers: `left` at the beginning and `right` at the end.
3. Add the smallest remaining element, followed by the largest remaining element.
4. If one middle element remains, add it to the sequence.
5. Sum the absolute differences between adjacent elements.
6. Add the absolute difference between the last and first elements.
7. Return the total.

## Example
**Input:** `[1, 2, 4, 8]`

**One optimal sequence:** `[1, 8, 2, 4]`

**Calculation:** `|1-8| + |8-2| + |2-4| + |4-1| = 7 + 6 + 2 + 3 = 18`

**Output:** `18`




