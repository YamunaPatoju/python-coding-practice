# ANARC05B - The Double Helix

## Problem Statement

You are given two strictly increasing integer sequences.

You may start from either sequence.

Whenever both sequences contain the same number (intersection point), you may either:

- Continue in the current sequence.
- Switch to the other sequence.

Find the maximum possible sum obtained by following such a path.

---

## Example

### Input

```text
First:
3 5 7 9 20 25 30 40 55 56 57 60 62

Second:
1 4 7 11 14 25 44 47 55 57 100
```

### Output

```text
450
```

---

## Approach

Use **Two Pointers**.

Maintain:

- Sum of current segment in first sequence.
- Sum of current segment in second sequence.

Whenever an intersection point occurs:

- Add the larger segment sum.
- Add the common element.
- Reset both segment sums.

Finally add the larger remaining segment.

---

## Algorithm

1. Initialize two pointers.
2. Traverse both arrays.
3. Accumulate sums separately.
4. At every common element:
   - Add the maximum segment sum.
   - Add the intersection value.
   - Reset segment sums.
5. After traversal, add the larger remaining sum.
6. Print the answer.

---

