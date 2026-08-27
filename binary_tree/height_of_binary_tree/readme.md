# Height of Binary Tree

## Problem Statement

Given the root of a binary tree, find the maximum depth or height of the tree.

The height of the binary tree is the number of edges from the root to the deepest node.

## Examples

### Example 1

**Input:**

```text
        12
       /  \
      8    18
     / \
    5   11
```

**Output:**

```text
2
```

### Example 2

**Input:**

```text
        1
       / \
      2   3
     /     \
    4       5
           / \
          6   7
```

**Output:**

```text
3
```

## Approach

- Use recursion to find the height of the binary tree.
- If the current node is `None`, return `-1` because height is measured in edges.
- Recursively find the height of the left subtree.
- Recursively find the height of the right subtree.
- Take the maximum of both subtree heights and add `1`.
- Return the height of the tree.

## Algorithm

1. If `root` is `None`, return `-1`.
2. Find the height of the left subtree.
3. Find the height of the right subtree.
4. Return `1 + max(left_height, right_height)`.
5. The returned value represents the number of edges from the root to the deepest node.

