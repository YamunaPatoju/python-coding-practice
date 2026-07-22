# 4 Sum - All Quadruples

## Problem Statement

Given an integer array `arr[]` and an integer `target`, find **all unique quadruples** whose sum equals the target.

Each quadruple must:

- Contain exactly four numbers.
- Be sorted internally.
- No duplicate quadruples should appear in the answer.

---

## Example 1

**Input**

```text
arr = [0, 0, 2, 1, 1]
target = 3
```

**Output**

```text
[[0, 0, 1, 2]]
```

---

## Example 2

**Input**

```text
arr = [10, 2, 3, 4, 5, 7, 8]
target = 23
```

**Output**

```text
[
 [2, 3, 8, 10],
 [2, 4, 7, 10],
 [3, 5, 7, 8]
]
```

---

## Example 3

**Input**

```text
arr = [0, 0, 2, 1, 1]
target = 2
```

**Output**

```text
[[0, 0, 1, 1]]
```

---

## Approach

Use **Sorting + Two Pointers**.

1. Sort the array.
2. Fix the first two elements using nested loops.
3. Use two pointers (`left` and `right`) to find the remaining two elements.
4. Skip duplicate values to avoid repeated quadruples.

---

## Algorithm

1. Sort the array.
2. Iterate over the first element `i`.
3. Iterate over the second element `j`.
4. Initialize:
   - `left = j + 1`
   - `right = n - 1`
5. Compute the sum:
   - If equal to target, store the quadruple.
   - If smaller, move `left`.
   - If larger, move `right`.
6. Skip duplicate values for all pointers.
7. Return all unique quadruples.

---

