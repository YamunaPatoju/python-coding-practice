# Flattening a Linked List

## Problem Statement

Given a linked list where every node contains `next` and `bottom` pointers, flatten all the linked lists into a single sorted linked list.

Each individual linked list is sorted in non-decreasing order, and the head nodes are also sorted.

The final linked list should use only the `bottom` pointers.

## Example

### Input

Multiple sorted linked lists connected using `next` pointers.

### Output

```text
5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 40 -> 45
```

## Approach

- Each linked list connected through the `next` pointer is already sorted using `bottom`.
- Use a **min-heap** to keep track of the smallest available node from each list.
- Insert the head of every list into the heap.
- Remove the smallest node from the heap and add it to the flattened list using the `bottom` pointer.
- If the removed node has a `bottom` node, insert that node into the heap.
- Continue until the heap becomes empty.
- The `next` pointers are not used in the final flattened list.

## Algorithm

1. If `head` is `None`, return `None`.
2. Create an empty min-heap.
3. Traverse the lists using `next`.
4. Insert every list's head into the heap.
5. Create a dummy node.
6. While the heap is not empty:
   - Remove the node with the smallest data.
   - Attach it using the `bottom` pointer.
   - If the node has a `bottom` node, insert it into the heap.
7. Set the last node's `bottom` pointer to `None`.
8. Return the flattened list.

