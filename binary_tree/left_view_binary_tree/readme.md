# Left View of Binary Tree

## Problem

Given the root of a binary tree, return the **left view** of the binary tree.

The left view consists of the nodes that are visible when the tree is viewed from the left side.

If the tree is empty, return an empty list.

## Approach

We use **Breadth-First Search (BFS)**, also called level-order traversal.

* Traverse the tree level by level using a queue.
* For each level, identify the **first node**.
* Add that first node to the result.
* Continue until all levels are processed.

The first node of every level is visible from the left side.

## Example

### Input

```text
        1
       / \
      2   3
     / \
    4   5
```

### Output

```text
[1, 2, 4]
```

### Explanation

* Level 1 → `1`
* Level 2 → `2`
* Level 3 → `4`

Therefore, the left view is:

```text
[1, 2, 4]
```

## Algorithm

1. If the root is `None`, return an empty list.
2. Create a queue and insert the root.
3. While the queue is not empty:

   * Store the number of nodes at the current level.
   * Process all nodes of that level.
   * Add the first node of the level to the result.
   * Add the left and right children to the queue.
4. Return the result.

