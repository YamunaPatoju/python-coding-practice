# Kth from End of Linked List

## Problem Statement

Given the head of a singly linked list and an integer `k`, return the data of the kth node from the end of the linked list.

If `k` is greater than the number of nodes, return `-1`.

## Example

### Input

```text
Linked List: 10 -> 20 -> 30 -> 40 -> 50
k = 2
```

### Output

```text
40
```

### Explanation

The nodes from the end are:

```text
1st -> 50
2nd -> 40
```

Therefore, the 2nd node from the end is `40`.

## Approach

Use the **two-pointer technique**.

- Maintain two pointers, `first` and `second`.
- Move `first` exactly `k` positions ahead.
- If `first` reaches `None` before completing `k` steps, then `k` is greater than the list length, so return `-1`.
- Move both pointers together until `first` reaches the end.
- At this point, `second` points to the kth node from the end.
- Return `second.data`.

## Algorithm

1. Set `first` and `second` to `head`.
2. Move `first` forward by `k` nodes.
3. If `first` becomes `None` before completing `k` moves, return `-1`.
4. Move `first` and `second` together until `first` reaches `None`.
5. Return `second.data`.

