# Diameter of a Binary Tree

## Problem Statement

Given the root of a binary tree, find the diameter of the binary tree.

The diameter is the number of edges on the longest path between any two nodes. The longest path may or may not pass through the root.

## Examples

### Example 1

**Input:**

```text
    1
   /
  2
 / \
3   4
```

**Output:**

```text
2
```

**Explanation:**

The longest path is:

```text
3 -> 2 -> 4
```

It contains `2` edges.

### Example 2

**Input:**

```text
        5
       / \
      8   6
     / \   \
    3   7   9
```

**Output:**

```text
4
```

**Explanation:**

The longest path is:

```text
3 -> 8 -> 5 -> 6 -> 9
```

It contains `4` edges.

## Approach

- Use recursion to calculate the height of every subtree.
- For each node, calculate the height of its left and right subtrees.
- The longest path passing through that node is `left_height + right_height`.
- Keep track of the maximum diameter found.
- Return the maximum diameter after traversing the entire tree.

## Algorithm

1. Initialize `ans = 0`.
2. Define a recursive function `height(node)`.
3. If `node` is `None`, return `0`.
4. Find the height of the left subtree.
5. Find the height of the right subtree.
6. Calculate the diameter passing through the current node:
   `left + right`.
7. Update the maximum diameter.
8. Return the height of the current node:
   `1 + max(left, right)`.
9. Return the maximum diameter.
