# Check If Circular Linked List
## Problem Statement

Given the `head` of a singly linked list, determine whether the linked list is circular.

A linked list is called **circular** if the last node points back to the first node instead of pointing to `None`.

An empty linked list is also considered circular.

> The linked list should not contain an inner loop. The cycle must return to the `head`.

## Examples

### Example 1

```text
1 → 2 → 3 → 4
↑           ↓
└───────────┘
```

**Output:**

```text
true
```

### Example 2

```text
1 → 2 → 3 → 4 → None
```

**Output:**

```text
false
```

## Approach

Start from the node after `head` and traverse the linked list.

- If we reach `None`, the linked list is not circular.
- If we reach `head` again, the linked list is circular.

We don't need a `visited` set because the problem guarantees that there is no inner loop.

## Algorithm

1. If `head` is `None`, return `True`.
2. Set `curr = head.next`.
3. Traverse while:
   ```text
   curr != None
   ```
   and
   ```text
   curr != head
   ```
4. Move:
   ```text
   curr = curr.next
   ```
5. Return:
   ```text
   curr == head
   ```

