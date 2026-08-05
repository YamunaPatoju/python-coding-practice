# Reverse a Linked List

## Problem Statement

Given the head of a singly linked list, reverse the linked list and return the head of the reversed list.

---

## Example 1

### Input

```
1 → 2 → 3 → 4
```

### Output

```
4 → 3 → 2 → 1
```

---

## Example 2

### Input

```
2 → 7 → 10 → 9 → 8
```

### Output

```
8 → 9 → 10 → 7 → 2
```

---

## Approach

We use three pointers:

- **prev** → Points to the previous node.
- **curr** → Current node being processed.
- **next_node** → Stores the next node before reversing the link.

For every node:

1. Save the next node.
2. Reverse the current node's pointer.
3. Move `prev` forward.
4. Move `curr` to the next node.

At the end, `prev` becomes the new head of the reversed linked list.

---

## Algorithm

1. Initialize:
   - `prev = None`
   - `curr = head`
2. Traverse the linked list while `curr` is not `None`.
3. Store the next node.
4. Reverse the current node's link.
5. Move both pointers one step ahead.
6. Return `prev`.

---

