# Construct Tree from Inorder & Preorder

## Problem

Given the **inorder** and **preorder** traversals of a binary tree, construct the binary tree and return its root.

The traversal arrays contain unique values.

## Approach

We use the properties of binary-tree traversals:

* **Preorder:** Root → Left → Right
* **Inorder:** Left → Root → Right

The first element of `preorder` is always the **root**.

After finding the root in `inorder`:

* Elements to the **left** belong to the left subtree.
* Elements to the **right** belong to the right subtree.

A dictionary is used to store the position of every value in the inorder array so that we can find the root position in `O(1)` time.

## Algorithm

1. Store every inorder value and its index in a dictionary.
2. Take the current element from preorder as the root.
3. Find the root's position in inorder.
4. Recursively construct the left subtree.
5. Recursively construct the right subtree.
6. Return the root.

## Example

### Input

```text
inorder  = [3, 1, 4, 0, 5, 2]
preorder = [0, 1, 3, 4, 2, 5]
```

