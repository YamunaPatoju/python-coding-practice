# All Duplicate Subtrees

## Problem

Given the root of a binary tree, find all **duplicate subtrees** present in the tree.

Two subtrees are considered duplicates when:

* They have the same structure.
* They contain the same node values at corresponding positions.

Return the root node of each duplicate subtree.

## Approach

Use **Postorder DFS** and create a unique representation for every subtree.

For each node:

1. Find the representation of its left subtree.
2. Find the representation of its right subtree.
3. Create a representation using:

   * Current node value
   * Left subtree representation
   * Right subtree representation
4. Store how many times this representation has appeared.
5. When a representation appears for the **second time**, add the current node to the result.

We add a duplicate only when its count becomes `2`, so the same duplicate subtree is not added multiple times.

## Example

Input:

```text id="qk4y8v"
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
```

Duplicate subtrees are:

```text id="w3q8zn"
    2        4
   /
  4
```

Output:

```text id="m7x2kp"
2 4
4
```

## Algorithm

```text id="q4v7na"
DFS(node)

    if node is None:
        return "#"

    left = DFS(node.left)
    right = DFS(node.right)

    representation =
        node.data + left + right

    increase count of representation

    if count == 2:
        add node to result

    return representation
```




