# Min and Max in Array

## Problem Statement

Given an array `arr[]`, find the minimum and maximum elements in the array.

Return them as:

```text
[min, max]
```

---

## Example 1

**Input**

```text
arr = [1, 4, 3, 5, 8, 6]
```

**Output**

```text
[1, 8]
```

---

## Example 2

**Input**

```text
arr = [12, 3, 15, 7, 9]
```

**Output**

```text
[3, 15]
```

---

## Approach

- Initialize both minimum and maximum with the first element.
- Traverse the array once.
- Update:
  - `mn` if a smaller element is found.
  - `mx` if a larger element is found.
- Return `[mn, mx]`.

---

