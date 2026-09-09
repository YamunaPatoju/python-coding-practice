# Sum Tree

## Problem

Given the root of a Binary Tree, check whether it is a Sum Tree.

A Sum Tree is a Binary Tree in which the value of every non-leaf node is equal to the sum of all nodes present in its left and right subtrees.

An empty tree and a leaf node are considered Sum Trees.

## Approach

Use postorder traversal.

For every node:

1. Find the sum of the left subtree.
2. Find the sum of the right subtree.
3. Check whether the current node value equals the sum of both subtrees.
4. Return the validity and total sum of the subtree.

## Example

Input:
[3, 1, 2]

Output:
True
