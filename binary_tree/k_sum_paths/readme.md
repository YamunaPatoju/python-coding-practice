# Print All K-Sum Paths in a Binary Tree

## Problem

Given a binary tree and an integer `k`, find all downward paths whose sum is equal to `k`.

A path:

* Can start from **any node**.
* Can end at **any node**.
* Must move **downward only** from parent to child.
* Does not have to start at the root or end at a leaf.
* Can contain **negative values**.

## Approach

Use **Depth First Search (DFS)** with a path list.

1. Traverse the tree recursively.
2. Add the current node to the current path.
3. Visit the left and right subtrees.
4. Starting from the current node, traverse the path backwards.
5. Keep calculating the sum.
6. Whenever the sum becomes `k`, store that portion of the path.
7. Remove the current node before returning to the parent.

Traversing the path backwards allows us to find paths that start at any node and end at the current node.

## Example

Input:

```text
k = 5

        1
       / \
      3  -1
     / \ / \
    2  1 4  5
      /   \   \
     1     2   6
```

Output:

```text
[3, 2]
[3, 1, 1]
[1, 3, 1]
[4, 1]
[1, -1, 4, 1]
[-1, 4, 2]
[5]
[1, -1, 5]
```


