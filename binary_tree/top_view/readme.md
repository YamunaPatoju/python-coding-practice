# Top View of Binary Tree

## Problem

Given the root of a binary tree, return its **top view**.

The top view contains the nodes visible when the binary tree is viewed from the top.

If multiple nodes have the same horizontal position, only the **topmost node** (closest to the root) is included.

The nodes should be returned from the **leftmost** horizontal position to the **rightmost**.

## Approach

Use **Breadth First Search (BFS)** and assign a **horizontal distance (HD)** to every node.

* Root has horizontal distance `0`.
* Left child has horizontal distance `HD - 1`.
* Right child has horizontal distance `HD + 1`.
* For each horizontal distance, store only the **first node** encountered.
* BFS guarantees that the first node encountered at a horizontal distance is the topmost node.
* Finally, sort the horizontal distances and return their corresponding node values.

## Example

Input:

```text
        1
       / \
      2   3
```

Horizontal distances:

```text
2 → -1
1 →  0
3 →  1
```

Output:

```text
[2, 1, 3]
```

