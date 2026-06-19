# Median of Two Sorted Arrays

## Problem Statement

Given two sorted arrays, find the median of the combined sorted array.

The median is the middle element of a sorted array. If the total number of elements is even, the median is the average of the two middle elements.

## Example 1

Input:

```text
nums1 = [1, 3]
nums2 = [2]
```

Output:

```text
2.0
```

## Example 2

Input:

```text
nums1 = [1, 2]
nums2 = [3, 4]
```

Output:

```text
2.5
```

## Approach

- Merge both arrays.
- Sort the merged array.
- Find the middle element.
- If the length is even, return the average of the two middle elements.
- Otherwise, return the middle element.
