# Reverse a Doubly Linked List in Groups of K

## Problem Statement

Given a doubly linked list containing `n` nodes, reverse every group of `k` nodes in the list.

If the number of nodes is not a multiple of `k`, the remaining nodes at the end should also be reversed.

## Examples

### Example 1

**Input:**  
`1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6`  
`k = 2`

**Output:**  
`2 <-> 1 <-> 4 <-> 3 <-> 6 <-> 5`

### Example 2

**Input:**  
`1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6`  
`k = 4`

**Output:**  
`4 <-> 3 <-> 2 <-> 1 <-> 6 <-> 5`

## Approach

- Traverse the doubly linked list.
- Reverse the `next` and `prev` pointers for every group of `k` nodes.
- Store the next group before changing the pointers.
- Connect the reversed group with the next group.
- Update the `prev` pointer of the next group.
- Continue until all nodes are processed.
- If fewer than `k` nodes remain, reverse them as well.

## Algorithm

1. If `head` is `None` or `k <= 1`, return `head`.
2. Set `curr = head` and `prev = None`.
3. Store the next node before changing the pointers.
4. Reverse the `next` and `prev` pointers of at most `k` nodes.
5. The original head becomes the tail of the reversed group.
6. Connect the tail to the next group.
7. Update the `prev` pointer of the next group.
8. Continue until the entire list is reversed in groups.
9. Return the new head.



linked_list/reverse_dll_in_groups/reverse_dll_in_groups.py
linked_list/reverse_dll_in_groups/README.md
