# Value Equal to Position

## Problem Statement

Given an array `arr[]`, find all elements whose value is equal to their **1-based position** in the array.

Return all such elements in a list.

---

## Example 1

**Input**

```text
arr = [15, 2, 45, 4, 7]
```

**Output**

```text
[2, 4]
```

**Explanation**

- Position 2 → Value = 2 ✓
- Position 4 → Value = 4 ✓

---

## Example 2

**Input**

```text
arr = [1]
```

**Output**

```text
[1]
```

---

## Approach

Traverse the array from left to right.

For every index:

- Compare the element with its **1-based position** (`index + 1`).
- If both are equal, add the element to the answer.

Finally, return the list of matching elements.

---

## Algorithm

1. Create an empty list `ans`.
2. Traverse the array.
3. If `arr[i] == i + 1`, append `arr[i]` to `ans`.
4. Return `ans`.

---

