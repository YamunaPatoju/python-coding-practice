# LCA in Binary Tree

## Problem

Given the root of a binary tree with unique values and two node values `n1` and `n2`, find the **Lowest Common Ancestor (LCA)** of the two nodes.

The LCA is the first common ancestor of both nodes from the bottom of the tree.

Both node values are guaranteed to be present in the binary tree.

## Approach

Use **Recursive DFS (Depth First Search)**.

For every node:

1. If the node is `None`, return `None`.
2. If the current node contains `n1` or `n2`, return the current node.
3. Search for `n1` and `n2` in the left subtree.
4. Search for them in the right subtree.
5. If both left and right return a node, the current node is the LCA.
6. If only one side returns a node, return that node.

## Example

Input:

```text
        2
       / \
      1   4
         / \
        3   9

n1 = 1
n2 = 4
```

Output:

```text
2
```


