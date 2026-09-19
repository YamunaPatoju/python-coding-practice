# Minimum in BST

## Problem

Given the root of a Binary Search Tree (BST), find the minimum element in the BST.

If the BST is empty, return `-1`.

## Approach

In a Binary Search Tree:

* All values in the left subtree are smaller than the current node.
* Therefore, the minimum value will always be the **leftmost node**.

### Steps

1. If the root is `None`, return `-1`.
2. Start from the root.
3. Keep moving to the left child while it exists.
4. When there is no left child, that node contains the minimum value.
5. Return its value.

## Example

### Input

```text
root = [5, 4, 6, 3, N, N, 7, 1]
```

### Output

```text
1
```

