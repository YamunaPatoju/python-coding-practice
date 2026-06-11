# Merge Two Sorted Arrays Without Extra Space

## Problem Statement

Given two sorted arrays `a[]` and `b[]`, merge them in sorted order without using any extra space.

After merging:

* `a[]` should contain the first `n` smallest elements.
* `b[]` should contain the remaining `m` largest elements.

## Example 1

**Input:**

a = [2, 4, 7, 10]

b = [2, 3]

**Output:**

a = [2, 2, 3, 4]

b = [7, 10]

## Example 2

**Input:**

a = [1, 5, 9, 10, 15, 20]

b = [2, 3, 8, 13]

**Output:**

a = [1, 2, 3, 5, 8, 9]

b = [10, 13, 15, 20]

## Approach

1. Initialize two pointers:

   * `i` at the last index of array `a`.
   * `j` at the first index of array `b`.
2. Compare `a[i]` and `b[j]`.
3. If `a[i]` is greater than `b[j]`, swap them.
4. Move `i` backward and `j` forward.
5. Repeat until all required swaps are completed.
6. Finally, sort both arrays.

