# Count Inversions

## Problem Statement

Given an array, find the number of inversions present in it.

An inversion is a pair of elements such that:

* The first element comes before the second element.
* The first element is greater than the second element.

## Example

**Input:**

```text
[2, 4, 1, 3, 5]
```

**Output:**

```text
3
```

**Explanation:**

The inversion pairs are:

```text
(2,1)
(4,1)
(4,3)
```

So the total inversion count is 3.

## My Approach

A simple nested loop solution checks every pair of elements, but it becomes very slow for large arrays.

To make it efficient, I used Merge Sort.

While merging two sorted halves, whenever an element from the right half is placed before an element from the left half, it means an inversion is found.

This allows us to count inversions while sorting the array.
