# Linked List Group Reverse

## Problem Statement

Given the head of a singly linked list, reverse every group of **k** nodes.

If the number of nodes left at the end is less than **k**, reverse them as well.

---

## Example 1

### Input

```
1 → 2 → 3 → 4 → 5 → 6
k = 2
```

### Output

```
2 → 1 → 4 → 3 → 6 → 5
```

---

## Example 2

### Input

```
1 → 2 → 3 → 4 → 5 → 6
k = 4
```

### Output

```
4 → 3 → 2 → 1 → 6 → 5
```

---

## Approach

- Reverse the first **k** nodes using three pointers:
  - `prev`
  - `curr`
  - `next`
- After reversing one group, recursively reverse the remaining list.
- Connect the last node of the reversed group to the head of the next reversed group.

---

## Algorithm

1. Initialize `prev`, `curr`, and `next`.
2. Reverse the first `k` nodes.
3. Recursively reverse the remaining linked list.
4. Connect the current group's last node to the next reversed group.
5. Return the new head (`prev`).

---

