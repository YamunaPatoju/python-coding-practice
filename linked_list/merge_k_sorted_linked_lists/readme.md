# Merge K Sorted Linked Lists

## Problem Statement

Given an array of `k` sorted linked lists, merge all the linked lists into a single sorted linked list.

## Example

### Input

```text
List 1: 1 -> 3 -> 7
List 2: 2 -> 4 -> 8
List 3: 9
```

### Output

```text
1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9
```

## Approach

- Use a **min-heap** to store the smallest available node from each linked list.
- Insert the head node of every non-empty list into the heap.
- Remove the smallest node from the heap and add it to the result.
- If that node has a next node, insert the next node into the heap.
- Continue until all nodes are processed.
- Use `id(node)` as a tie-breaker when two nodes have the same data value.

## Algorithm

1. Create an empty min-heap.
2. Insert the head of every non-empty linked list.
3. Create a dummy node.
4. While the heap is not empty:
   - Extract the smallest node.
   - Attach it to the result list.
   - Insert its next node into the heap if it exists.
5. Set the last node's `next` to `None`.
6. Return `dummy.next`.



## Language

Python 3
