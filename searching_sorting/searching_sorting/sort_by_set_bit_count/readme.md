# Sort by Set Bit Count

## Problem Statement

Given an array `arr[]` of integers, sort the array in **descending order** according to the number of **set bits (1s)** in the binary representation of each element.

If two elements have the same number of set bits, maintain their **original relative order** (stable sort).

---

## Example 1

**Input**

```text
arr = [5, 2, 3, 9, 4, 6, 7, 15, 32]
```

**Output**

```text
[15, 7, 5, 3, 9, 6, 2, 4, 32]
```

---

## Example 2

**Input**

```text
arr = [1, 2, 3, 4, 5, 6]
```

**Output**

```text
[3, 5, 6, 1, 2, 4]
```

---

## Approach

Use Python's built-in **stable sort**.

- Count the number of set bits in each element.
- Sort the array in **descending order** based on the set-bit count.
- Since Python's sort is stable, elements with the same number of set bits remain in their original order.

---

## Algorithm

1. Traverse the array.
2. Count the number of set bits using:

```text
bin(x).count('1')
```

3. Sort the array in descending order using the set-bit count as the key.
4. Return the sorted array.

---

