# Remove Cycle in Linked List

## Problem Statement

Given the head of a singly linked list, remove the cycle (loop) if it exists.

After removing the loop, the linked list should become a normal singly linked list.

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
1 → 2 → 3 → 4 → NULL
```

---

## Example 2

### Input

```
1 → 2 → 3 → NULL
```

### Output

```
1 → 2 → 3 → NULL
```

---

## Approach

Use **Floyd's Cycle Detection Algorithm**.

1. Detect whether a loop exists.
2. If no loop exists, return.
3. If a loop exists:
   - Find the starting node of the loop.
   - Find the node just before the loop starts.
   - Make its `next` pointer `None`.

This removes the cycle without changing the remaining list.

---

## Algorithm

1. Initialize two pointers:
   - slow
   - fast
2. Detect loop using Floyd's Algorithm.
3. If no loop is found, return.
4. Move `slow` to head.
5. Move both pointers one step until their next pointers become equal.
6. Set `fast.next = None`.


---

