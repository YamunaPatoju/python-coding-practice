# Detect Loop in Linked List

## Problem Statement

Given the head of a singly linked list, determine whether the linked list contains a loop (cycle).

A loop exists if the last node points back to any previous node instead of `NULL`.

---

## Example 1

### Input

```
1 → 2 → 3 → 4
     ↑       ↓
     └───────┘
```

### Output

```
True
```

---

## Example 2

### Input

```
1 → 2 → 3 → 4 → NULL
```

### Output

```
False
```

---

## Approach

Use **Floyd's Cycle Detection Algorithm (Tortoise and Hare).**

- Maintain two pointers:
  - **slow** moves one step at a time.
  - **fast** moves two steps at a time.
- If there is a loop, both pointers will eventually meet.
- If `fast` reaches `NULL`, there is no loop.

---

## Algorithm

1. Initialize `slow` and `fast` to the head.
2. Move:
   - `slow = slow.next`
   - `fast = fast.next.next`
3. If `slow == fast`, return `True`.
4. If traversal ends, return `False`.

---

