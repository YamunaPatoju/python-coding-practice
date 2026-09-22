# Lowest Common Ancestor in a BST

## Problem

Given a Binary Search Tree (BST) with unique node values and two nodes `n1` and `n2`, find their Lowest Common Ancestor (LCA).

The LCA is the deepest node that has both `n1` and `n2` as descendants.

A node can also be a descendant of itself.

## Approach

We use the BST property to find the LCA efficiently.

For the current node:

* If both nodes are smaller than the current node, move to the **left subtree**.
* If both nodes are greater than the current node, move to the **right subtree**.
* Otherwise, the current node is the LCA.

In the GFG version, `n1` and `n2` are **Node objects**, so we compare their `.data` values.

## Algorithm

1. Start from the root.
2. If `n1.data` and `n2.data` are both smaller than `root.data`, move left.
3. If `n1.data` and `n2.data` are both greater than `root.data`, move right.
4. Otherwise, return the current node.
5. Continue until the LCA is found.

## Example

### Input

```text
root = [2, 1, 3]
n1 = 1
n2 = 3
```

### Output

```text
2
```


