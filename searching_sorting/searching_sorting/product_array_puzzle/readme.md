# Product Array Puzzle

## Problem Statement

Given an array `arr[]`, construct a product array `res[]` such that:

```text
res[i] = product of all elements of arr except arr[i]
```

Return the resultant array.

**Note:** Do not use division.

---

## Example 1

**Input**

```text
arr = [10, 3, 5, 6, 2]
```

**Output**

```text
[180, 600, 360, 300, 900]
```

**Explanation**

```text
res[0] = 3 × 5 × 6 × 2 = 180
res[1] = 10 × 5 × 6 × 2 = 600
res[2] = 10 × 3 × 6 × 2 = 360
res[3] = 10 × 3 × 5 × 2 = 300
res[4] = 10 × 3 × 5 × 6 = 900
```

---

## Example 2

**Input**

```text
arr = [12, 0]
```

**Output**

```text
[0, 12]
```

---

## Approach

Use **Prefix Product** and **Suffix Product**.

- Prefix product stores the product of all elements before the current index.
- Suffix product stores the product of all elements after the current index.
- Multiply both values to get the required answer.

This avoids division and works correctly even when the array contains zeros.

---

## Algorithm

1. Create a result array initialized with `1`.
2. Traverse from left to right:
   - Store prefix product.
3. Traverse from right to left:
   - Multiply suffix product into the result.
4. Return the result array.

---

