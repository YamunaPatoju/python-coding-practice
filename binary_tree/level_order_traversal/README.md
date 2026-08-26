# Level Order Traversal

## Problem Statement

Given the root of a binary tree, return its level order traversal.

Level order traversal is a Breadth-First Search (BFS) traversal of the binary tree. It visits nodes level by level, processing nodes from left to right.

## Example

### Input

```text
        1
       / \
      2   3
```

### Output

```text
[1, 2, 3]
```

## Approach

- Use a queue to perform Breadth-First Search (BFS).
- Insert the root node into the queue.
- Remove one node from the front of the queue.
- Add its data to the result.
- Add its left child and right child to the queue if they exist.
- Continue until the queue becomes empty.

## Algorithm

1. If the root is `None`, return an empty list.
2. Create a queue and add the root node.
3. Create an empty result list.
4. While the queue is not empty:
   - Remove the front node.
   - Add its data to the result.
   - Add its left child to the queue if it exists.
   - Add its right child to the queue if it exists.
5. Return the result.
