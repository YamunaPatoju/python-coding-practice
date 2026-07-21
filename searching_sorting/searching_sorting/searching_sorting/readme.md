# Pair With Difference

## Problem Statement

Given an array `arr[]` and an integer `x`, determine whether there exists a pair of elements whose **absolute difference** is exactly `x`.

Return:

- `True` if such a pair exists.
- `False` otherwise.

---

## Example 1

**Input**

```text
arr = [5, 20, 3, 2, 5, 80]
x = 78
```

**Output**

```text
True
```

**Explanation**

The pair `(2, 80)` has an absolute difference of:

```text
80 - 2 = 78
```

---

## Example 2

**Input**

```text
arr = [90, 70, 20, 80, 50]
x = 45
```

**Output**

```text
False
```

**Explanation**

No pair has an absolute difference of `45`.

---

## Example 3

**Input**

```text
arr = [1]
x = 1
```

**Output**

```text
False
```

---

## Approach

Use the **Sorting + Two Pointer** technique.

1. Sort the array.
2. Maintain two pointers:
   - `i` → left pointer
   - `j` → right pointer
3. Compute the difference:
   - If equal to `x`, return `True`.
   - If smaller, move `j`.
   - If larger, move `i`.
4. Continue until the end of the array.

This efficiently checks all possible pairs.

---

## Algorithm

1. Sort the array.
2. Initialize `i = 0` and `j = 1`.
3. While `j < n`:
   - Compute `diff = arr[j] - arr[i]`.
   - If `diff == x`, return `True`.
   - If `diff < x`, increment `j`.
   - Otherwise, increment `i`.
   - If `i == j`, increment `j`.
4. If no pair is found, return `False`.

---

