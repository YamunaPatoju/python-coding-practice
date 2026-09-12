# Largest Subtree Sum

## Problem

Given a binary tree, find the subtree with the maximum sum and return its sum.

## Approach

Use postorder traversal.

For every node:

1. Find the sum of the left subtree.
2. Find the sum of the right subtree.
3. Add the current node value.
4. Update the maximum sum.
5. Return the current subtree sum to the parent.

## Example

Input:

```text
        1
       / \
     -2   3
     / \ / \
   -4  1 2  6
```

Subtree containing `3`:

```text
2 + 6 + 3 = 11
```

Output:

```text
11
```


