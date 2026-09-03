# Bottom View of Binary Tree

## Problem

Given the root of a binary tree, return its **bottom view**.

The bottom view contains the nodes visible when the binary tree is viewed from the bottom.

If multiple nodes have the same horizontal distance, the **latter node in level order traversal** is considered.

The nodes should be returned from the **leftmost** horizontal distance to the **rightmost**.

## Approach

Use **Breadth First Search (BFS)** with a horizontal distance.

* Root has horizontal distance `0`.
* Left child has horizontal distance `HD - 1`.
* Right child has horizontal distance `HD + 1`.
* Store the node value for every horizontal distance.
* Unlike top view, **overwrite** the value whenever another node is encountered at the same horizontal distance.
* Because BFS processes nodes in level order, the last encountered node is the required bottom-most node.
* Sort the horizontal distances and return their values.

## Example

Input:

```text id="3cn1kx"
        1
       / \
      2   3
     / \   \
    4   5   6
```

Horizontal distances:

```text id="qv2d8m"
4 → -2
2 → -1
5 →  0
3 →  1
6 →  2
```

Output:

```text id="6p1j8r"
[4, 2, 5, 3, 6]
```

