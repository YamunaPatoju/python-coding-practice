# Count Inversions

## Problem Statement

Given an array, count the number of **inversions**.

An inversion is a pair `(i, j)` such that:

- `i < j`
- `arr[i] > arr[j]`

---

## Example 1

**Input**

```text
[2,4,1,3,5]
```

**Output**

```text
3
```

Inversions:

```text
(2,1)
(4,1)
(4,3)
```

---

## Example 2

**Input**

```text
[2,3,4,5,6]
```

**Output**

```text
0
```

---

## Approach

A brute-force solution checks every pair in **O(n²)**.

A better solution uses **Merge Sort**.

During merging:

- If the left element is greater than the right element,
- then all remaining elements in the left half are also greater.

This directly gives the inversion count.

---

## Algorithm

1. Divide the array into two halves.
2. Count inversions in the left half.
3. Count inversions in the right half.
4. Count split inversions during merge.
5. Return the total count.

---

