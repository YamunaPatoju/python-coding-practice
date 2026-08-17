# Sort a K-Sorted Doubly Linked List

## Problem

Given a doubly linked list where every node is at most `K` positions away from its correct position in the sorted list, sort the linked list.

All elements are distinct.

## Approach

Use a **Min Heap**.

Since every element is at most `K` positions away from its sorted position, the smallest element among the next `K + 1` nodes can be placed correctly.

Steps:

1. Insert the first `K + 1` nodes into a min heap.
2. Remove the smallest node from the heap.
3. Add it to the sorted doubly linked list.
4. Insert the next node into the heap.
5. Continue until all nodes are processed.
6. Maintain both `next` and `prev` pointers.

A counter is used along with the node value in the heap so that duplicate values do not cause node comparison errors.

## Example

### Input

```text
6 5 3 2 8 10 9
