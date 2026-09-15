# Min Distance Between Two Nodes in Binary Tree

## Problem

Given a binary tree and two node values `a` and `b`, find the **minimum distance** between the two nodes.

The distance is defined as the minimum number of **edges** between the two nodes.

Both nodes are guaranteed to exist in the tree, and all node values are unique.

## Approach

The minimum distance between two nodes can be found using their **Lowest Common Ancestor (LCA)**.

### Steps

1. Find the LCA of nodes `a` and `b`.
2. Find the distance from the LCA to node `a`.
3. Find the distance from the LCA to node `b`.
4. Add both distances.

The result is:

```text
Distance(a, b) = Distance(LCA, a) + Distance(LCA, b)
```

