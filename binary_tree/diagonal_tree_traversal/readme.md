# Diagonal Tree Traversal

## Problem

Given a Binary Tree, return its **diagonal traversal**.

Nodes that lie on the same diagonal are grouped together. If diagonal elements are present in both the left and right subtrees, the **left subtree elements are taken first**, followed by the right subtree elements.

## Approach

Use a **queue** to process diagonal elements.

1. Start with the root and add it to the queue.
2. Take a node from the queue.
3. Traverse along its right subtree because nodes connected through right edges belong to the same diagonal.
4. Whenever a node has a left child, add that left child to the queue for processing in the next diagonal.
5. Continue until the queue becomes empty.

This processes the diagonals from top to bottom while maintaining the required left-subtree-first order.

## Example

### Input

```text
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

### Output

```text
[8, 10, 14, 3, 6, 7, 13, 1, 4]
```


