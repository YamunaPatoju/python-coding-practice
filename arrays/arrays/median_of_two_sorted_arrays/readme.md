# Median of Two Sorted Arrays

## Problem Statement

Given two sorted arrays, find the median of the combined array.

The median is the middle element of a sorted array. If the array has an even number of elements, the median is the average of the two middle elements.

## Example 1

Input:

```text
a = [1, 3]
b = [2]
```

Output:

```text
2
```

Explanation:

Combined array:

```text
[1, 2, 3]
```

Middle element = 2

## Example 2

Input:

```text
a = [1, 2]
b = [3, 4]
```

Output:

```text
2.5
```

Explanation:

Combined array:

```text
[1, 2, 3, 4]
```

Median = (2 + 3) / 2 = 2.5

## Approach

1. Merge both arrays.
2. Sort the merged array.
3. Find the middle index.
4. If the total number of elements is odd, return the middle element.
5. If the total number of elements is even, return the average of the two middle elements.

