# Normal BST to Balanced BST

## Problem

Given the root of a Binary Search Tree (BST), modify and return the BST such that it becomes balanced and has the **minimum possible height**.

If there is more than one possible balanced BST, any valid answer can be returned.

## Approach

A BST's inorder traversal always gives its elements in **sorted order**.

We use this property to create a balanced BST:

1. Perform inorder traversal and store all node values in a list.
2. The values are now sorted.
3. Select the middle element as the root.
4. Recursively build the left subtree using the left half.
5. Recursively build the right subtree using the right half.
6. Return the newly constructed root.

Choosing the middle element at every step keeps the left and right subtrees as balanced as possible.

## Algorithm

```text
1. Perform inorder traversal of the BST.
2. Store all node values in a sorted array.
3. Choose the middle element as the root.
4. Recursively build the left subtree from the left half.
5. Recursively build the right subtree from the right half.
6. Return the new root.
```



