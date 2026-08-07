# Remove Duplicates from a Sorted Linked List

## Problem Statement

Given the head of a sorted singly linked list, remove all duplicate nodes so that each element appears only once.

The resulting linked list should remain sorted.

---

## Example 1

### Input

```text
2 → 2 → 4 → 5
```

### Output

```text
2 → 4 → 5
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

The linked list is already sorted, so duplicate values will always be next to each other.

Use a pointer `curr` to traverse the list.

- If `curr.data == curr.next.data`, skip the duplicate node.
- Otherwise, move `curr` to the next node.

No extra data structure is required.

---

## Algorithm

1. Set `curr = head`.
2. Traverse the linked list while `curr` and `curr.next` exist.
3. If the current and next nodes contain the same value:
   ```text
   curr.next = curr.next.next
   ```
4. Otherwise, move `curr` to the next node.
5. Return `head`.

---

