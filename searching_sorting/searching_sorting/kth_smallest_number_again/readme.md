# Kth Smallest Number Again

## Problem Statement

You are given `N` ranges of integers.

All numbers from these ranges are considered only once (distinct numbers), even if the ranges overlap.

For each query `K`, find the **Kth smallest number** in the combined sorted sequence.

If the Kth smallest number does not exist, print `-1`.

---

## Example

### Input

```text
Ranges:
[1, 5]

Queries:
1
3
6
```

### Output

```text
1
3
-1
```

---

## Approach

Overlapping ranges may contain duplicate numbers.

To avoid duplicates:

1. Sort all intervals.
2. Merge overlapping or adjacent intervals.
3. Compute the number of integers in each merged interval.
4. Build a Prefix Sum array storing cumulative counts.
5. For each query:
   - Use Binary Search to find the interval containing the Kth number.
   - Compute the answer directly.

---

## Algorithm

1. Read all intervals.
2. Sort the intervals.
3. Merge overlapping intervals.
4. Build a prefix count array.
5. For each query:
   - If `K` is greater than the total number of elements, print `-1`.
   - Otherwise:
     - Binary Search on the prefix count array.
     - Find the corresponding interval.
     - Compute the exact Kth number.

---

