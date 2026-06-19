# Minimum Swaps and K Together

## Problem Statement

Given an array `arr` and a number `k`, find the minimum number of swaps required to bring all elements less than or equal to `k` together.

A swap can be performed between any two positions in the array.

## Example 1

Input:

```text
arr = [2, 1, 5, 6, 3]
k = 3
```

Output:

```text
1
```
## Example 2

Input:

```text
arr = [2, 7, 9, 5, 8, 7, 4]
k = 6
```

Output:

```text
2
```
## Approach

First, count how many elements are less than or equal to `k`.

This count becomes the window size because all these elements need to be grouped together.

Then:

1. Count the elements greater than `k` in the first window.
2. These elements are considered "bad" elements.
3. Slide the window through the array.
4. Update the count of bad elements for each window.
5. The minimum number of bad elements in any window is the answer.

