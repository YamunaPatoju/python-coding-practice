# Remove Duplicates from an Unsorted Linked List

## Problem Statement

Given the head of an unsorted singly linked list, remove duplicate elements.

When a value appears multiple times, keep the **first occurrence** and remove all later occurrences.

---

## Example 1

### Input

```text
5 → 2 → 2 → 4
```

### Output

```text
5 → 2 → 4
```

---

## Example 2

### Input

```text
2 → 2 → 2 → 2 → 2
```

### Output

```text
2
```

---

## Approach

Since the linked list is **unsorted**, duplicate values may not be adjacent.

Use a **set** called `seen` to store values that have already appeared.

Maintain two pointers:

- `curr` → current node
- `prev` → previous node

For every node:

- If its value is already in `seen`, remove it by:
  ```text
  prev.next = curr.next
  ```
- Otherwise, add its value to `seen` and move `prev`.

---

## Algorithm

1. Create an empty set `seen`.
2. Set `curr = head` and `prev = None`.
3. Traverse the linked list.
4. If `curr.data` is already in `seen`:
   - Remove the current node.
5. Otherwise:
   - Add `curr.data` to `seen`.
   - Move `prev` to `curr`.
6. Move `curr` to the next node.
7. Return `head`.

---

