# Invert Binary Tree

## Problem Statement

Given the root of a binary tree, invert the tree and return its root.

Inverting a binary tree means swapping the left and right children of every node.

## Examples

### Example 1

**Input:**

```text
        4
       / \
      2   7
     / \ / \
    1  3 6  9
```

**Output:**

```text
        4
       / \
      7   2
     / \ / \
    9  6 3  1
```

### Example 2

**Input:**

```text
    2
   / \
  1   3
```

**Output:**

```text
    2
   / \
  3   1
```

### Example 3

**Input:**

```text
[]
```

**Output:**

```text
[]
```

## Approach

- Use recursion to visit every node.
- At each node, swap its left and right children.
- Recursively invert the left subtree.
- Recursively invert the right subtree.
- Return the root after all nodes are inverted.

## Algorithm

1. If `root` is `None`, return `None`.
2. Swap `root.left` and `root.right`.
3. Recursively invert the left subtree.
4. Recursively invert the right subtree.
5. Return the root.

