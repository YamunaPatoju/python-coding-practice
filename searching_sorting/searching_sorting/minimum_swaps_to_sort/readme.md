# Minimum Swaps to Sort

## Problem Statement

Given an array `arr[]` of distinct elements, determine the **minimum number of swaps** required to sort the array in **strictly increasing order**.

---

## Example 1

**Input**

```text
arr = [2, 8, 5, 4]
```

**Output**

```text
1
```

**Explanation**

Swap:

```text
8 ↔ 4
```

Sorted array:

```text
[2, 4, 5, 8]
```

---

## Example 2

**Input**

```text
arr = [10, 19, 6, 3, 5]
```

**Output**

```text
2
```

---

## Example 3

**Input**

```text
arr = [1, 3, 4, 5, 6]
```

**Output**

```text
0
```

---

## Approach

This problem is solved using **Cycle Detection**.

### Idea

- Pair each element with its original index.
- Sort these pairs based on element values.
- Every misplaced element forms part of a cycle.
- If a cycle contains `k` elements, it requires:

```text
k - 1
```

swaps.

Total swaps = sum of `(cycle size - 1)` for all cycles.

---

## Algorithm

1. Store each element with its original index.
2. Sort the array of pairs.
3. Maintain a `visited` array.
4. Traverse every element.
5. If an element is already in the correct position or visited, skip it.
6. Otherwise, traverse the entire cycle.
7. Add:

```text
cycle_size - 1
```

to the answer.
8. Return the total swaps.

---

