# Check for BST

## Problem

Given a binary tree, check whether it is a valid Binary Search Tree (BST).

A binary tree is a BST if:

* Every node in the left subtree has a smaller value.
* Every node in the right subtree has a greater value.
* Both left and right subtrees are also BSTs.

Return `True` if the tree is a BST, otherwise return `False`.

## Approach

We use the **range method**.

For every node, maintain the valid range of values that the node can contain.

Initially, the root can contain any value:

```text
(-∞, +∞)
```

For a node with value `x`:

* Its left subtree must contain values in `(low, x)`.
* Its right subtree must contain values in `(x, high)`.

If any node goes outside its allowed range, the tree is not a BST.

## Example

### Input

```text
root = [2, 1, 3, N, N, N, 5]
```

### Output

```text
True
```




