# Merge Without Extra Space

## Problem Statement

Given two sorted arrays `a[]` and `b[]`, merge them in sorted order **without using any extra space**.

After merging:

- `a[]` should contain the first `n` smallest elements.
- `b[]` should contain the remaining `m` largest elements.

---

## Example 1

**Input**

```text
a = [2, 4, 7, 10]
b = [2, 3]
```

**Output**

```text
a = [2, 2, 3, 4]
b = [7, 10]
```

---

## Example 2

**Input**

```text
a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
```

**Output**

```text
a = [1, 2, 3, 5, 8, 9]
b = [10, 13, 15, 20]
```

---

## Approach

Use the **Gap Method** (inspired by Shell Sort).

Instead of using extra space:

1. Treat both arrays as one combined array.
2. Compare elements that are `gap` distance apart.
3. Swap if they are out of order.
4. Gradually reduce the gap until it becomes `1`.

This merges both arrays in-place.

---

## Algorithm

1. Compute:

```text
gap = ceil((n + m) / 2)
```

2. Compare elements `gap` apart.
3. Swap whenever needed.
4. Reduce the gap:

```text
gap = ceil(gap / 2)
```

5. Stop when the gap becomes `1`.

---

