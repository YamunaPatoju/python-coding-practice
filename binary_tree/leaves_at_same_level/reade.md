# Leaves at Same Level or Not

## Problem

Given the root of a binary tree, check whether all leaf nodes are present at the same level.

A leaf node is a node that has no left or right child.

## Approach

Use Depth First Search (DFS).

- Track the level of the first leaf node.
- For every other leaf node, compare its level with the first leaf's level.
- If all leaf nodes are at the same level, return `True`.
- Otherwise, return `False`.

## Example

Input:
[12, 5, 7, 3, N, N, 1]

Output:
True

## Example

Input:
[12, 5, 7, 3, N]

Output:
False
