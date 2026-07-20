# Missing And Repeating

## Problem Statement

Given an unsorted array `arr[]` of size `n` containing numbers from **1 to n**, exactly one number is **missing** and one number is **repeated**.

Return the repeating number first, followed by the missing number.

---

## Example 1

**Input**

```text
arr = [2, 2]
```

**Output**

```text
[2, 1]
```

**Explanation**

- Repeating number = 2
- Missing number = 1

---

## Example 2

**Input**

```text
arr = [1, 3, 3]
```

**Output**

```text
[3, 2]
```

---

## Example 3

**Input**

```text
arr = [4, 3, 6, 2, 1, 1]
```

**Output**

```text
[1, 5]
```

---

## Approach

Use the **Bit Manipulation (XOR)** technique.

1. XOR all elements of the array.
2. XOR all numbers from `1` to `n`.
3. The result is `missing XOR repeating`.
4. Find the rightmost set bit to divide numbers into two groups.
5. XOR each group separately to obtain the two numbers.
6. Check which number appears twice in the array.
7. Return `[repeating, missing]`.

This avoids extra space and runs in linear time.

---

## Algorithm

1. Compute XOR of all array elements and numbers from `1` to `n`.
2. Find the rightmost set bit.
3. Divide numbers into two groups based on this bit.
4. XOR each group separately.
5. Determine which result is the repeating number.
6. Return the answer.

---
