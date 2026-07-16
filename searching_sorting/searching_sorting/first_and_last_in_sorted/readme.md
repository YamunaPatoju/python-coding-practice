# First and Last Occurrence in a Sorted Array

## Problem Statement

Given a sorted array `arr[]` (which may contain duplicate elements) and an integer `x`, find the indices of the **first** and **last** occurrence of `x`.

If `x` is not present in the array, return `[-1, -1]`.

---

## Example 1

**Input**

```text
arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
x = 5
```

**Output**

```text
[2, 5]
```

---

## Example 2

**Input**

```text
arr = [1, 3, 5, 5, 5, 5, 7, 123, 125]
x = 7
```

**Output**

```text
[6, 6]
```

---

## Example 3

**Input**

```text
arr = [1, 2, 3]
x = 4
```

**Output**

```text
[-1, -1]
```

---

## Approach

This problem is solved using **Binary Search**.

- Perform one binary search to find the **first occurrence**.
- Perform another binary search to find the **last occurrence**.
- Return both indices.

---

## Algorithm

1. Initialize `low`, `high`, and `ans`.
2. For the first occurrence:
   - If `arr[mid] == x`, store `mid` and continue searching on the left.
3. For the last occurrence:
   - If `arr[mid] == x`, store `mid` and continue searching on the right.
4. Return both indices.

---

