# Split a Linked List into Two Halves

**Difficulty:** Easy

## Problem Statement

Given a **circular linked list**, split it into two circular linked lists.

If the number of nodes is odd, the **first linked list must contain one more node** than the second linked list.

Both resulting lists must remain circular.

## Examples

### Example 1

**Input:**

```text
10 → 4 → 9 → back to 10
```

**Output:**

```text
First:  10 → 4 → back to 10
Second: 9 → back to 9
```

The first list contains 2 nodes and the second contains 1 node.

### Example 2

**Input:**

```text
10 → 4 → 9 → 10 → back to 10
```

**Output:**

```text
First:  10 → 4 → back to 10
Second: 9 → 10 → back to 9
```

Both lists contain 2 nodes.

## Approach

Use the **Slow and Fast Pointer** technique.

- `slow` moves one node at a time.
- `fast` moves two nodes at a time.
- When `fast` reaches the end of the circular list, `slow` points to the last node of the first half.

Then:

```text
head1 = head
head2 = slow.next
```

Finally, modify the `next` pointers:

```text
slow.next = head1
fast.next = head2
```

This makes both halves circular.

## Algorithm

1. Handle an empty or single-node list.
2. Initialize:
   ```text
   slow = head
   fast = head
   ```
3. Move `slow` by one step and `fast` by two steps.
4. Stop when `fast` reaches the end of the circular list.
5. Set:
   ```text
   head1 = head
   head2 = slow.next
   ```
6. Connect the last node of the first half to `head1`.
7. Connect the last node of the second half to `head2`.
8. Return both heads.

