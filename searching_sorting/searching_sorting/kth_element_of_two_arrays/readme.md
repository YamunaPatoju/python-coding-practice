# K-th Element of Two Arrays

## Problem Statement

Given two **sorted arrays** `a[]` and `b[]`, and an integer `k`, find the element that would appear at the **k-th position** in the merged sorted array without actually merging the arrays.

---

## Example 1

**Input**

```text
a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
```

**Output**

```text
6
```

**Explanation**

Merged array:

```text
[1, 2, 3, 4, 6, 7, 8, 9, 10]
```

The 5th element is **6**.

---

## Example 2

**Input**

```text
a = [1, 4, 8, 10, 12]
b = [5, 7, 11, 15, 17]
k = 6
```

**Output**

```text
10
```

---

## Approach

Instead of merging both arrays (`O(n + m)`), use **Binary Search** on the smaller array.

Partition both arrays such that:

- Left partition contains exactly `k` elements.
- Every element in the left partition is less than or equal to every element in the right partition.

If the partition is valid:

```text
max(left1, left2)
```

is the k-th smallest element.

---

## Algorithm

1. Always binary search on the smaller array.
2. Choose a partition in the first array.
3. Compute the corresponding partition in the second array.
4. Check if the partition is valid:
   - `left1 <= right2`
   - `left2 <= right1`
5. If valid, return the maximum element from the left partitions.
6. Otherwise, adjust the binary search range.
7. Continue until the correct partition is found.

---

