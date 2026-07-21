# Search Array with Adjacent Difference at Most K

## Problem Statement

Given a **step array** `arr[]`, an integer `k`, and a key `x`, find the **first occurrence** of `x`.

A **step array** is an array where the absolute difference between every pair of adjacent elements is at most `k`.

If the key is not present, return `-1`.

---

## Example 1

**Input**

```text
arr = [4, 5, 6, 7, 6]
k = 1
x = 6
```

**Output**

```text
2
```

**Explanation**

The first occurrence of `6` is at index `2`.

---

## Example 2

**Input**

```text
arr = [20, 40, 50]
k = 20
x = 70
```

**Output**

```text
-1
```

**Explanation**

The element `70` is not present in the array.

---

## Approach

A normal linear search checks every element one by one.

Since adjacent elements differ by at most `k`, we can **skip several indices** at a time.

The minimum jump is calculated as:

```text
abs(arr[i] - x) // k
```

To avoid staying at the same position, always jump at least one step:

```text
max(1, abs(arr[i] - x) // k)
```

This makes the search faster while maintaining correctness.

---

## Algorithm

1. Start from index `0`.
2. If `arr[i] == x`, return `i`.
3. Otherwise, calculate the jump:

```text
jump = max(1, abs(arr[i] - x) // k)
```

4. Move to the next index using the jump.
5. Repeat until the end of the array.
6. If the element is not found, return `-1`.

---
