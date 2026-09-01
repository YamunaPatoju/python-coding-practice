# Right View of Binary Tree

## Problem

Given the root of a binary tree, return the nodes visible when the tree is viewed from the right side.

The right view contains the rightmost node from each level of the binary tree.

## Approach

Use **Breadth First Search (BFS)** with a queue.

1. Start with the root node.
2. Process the tree level by level.
3. For every level, identify the last node.
4. Add that node's value to the result.
5. Add the left and right children to the queue.
6. Continue until all levels are processed.

## Example

Input:

```text
        1
       / \
      2   3
         / \
        4   5
```

Output:

```text
[1, 3, 5]
```

