# Reverse a Doubly Linked List in Groups of K

## Problem Statement

Given a doubly linked list containing `n` nodes, reverse every group of `k` nodes in the list.

If the number of nodes is not a multiple of `k`, the remaining nodes at the end should also be reversed.

## Examples

### Example 1

**Input:**
```text
1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6
k = 2
**Approach**
Traverse the doubly linked list.
Reverse the next and prev pointers for every group of k nodes.
Store the next group before changing the pointers.
Connect the reversed group with the next group.
Update the prev pointer of the next group.
Continue until all nodes are processed.
If fewer than k nodes remain, reverse them as well.
**Algorithm**
If head is None or k <= 1, return head.
Set curr = head and prev = None.
Reverse the pointers of at most k nodes.
The original head becomes the tail of the reversed group.
Connect the tail to the next group.
Update the prev pointer of the next group.
Return the new head.
