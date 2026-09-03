# Zig-Zag Tree Traversal

## Problem

Given the root of a binary tree, find the **zig-zag level order traversal** of the tree.

In zig-zag traversal:

* Odd-numbered levels are traversed from **left to right**.
* Even-numbered levels are traversed from **right to left**.

## Approach

Use **Breadth First Search (BFS)** to process the tree level by level.

1. Start with the root in a queue.
2. Process one level at a time.
3. Store the nodes of the current level in a temporary list.
4. If the current level should be traversed from right to left, reverse the temporary list.
5. Add the level to the final result.
6. Alternate the traversal direction for the next level.

## Example

Input:

```text
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

Level 1: Left → Right

```text
[1]
```

Level 2: Right → Left

```text
[3, 2]
```

Level 3: Left → Right

```text
[4, 5, 6, 7]
```

Output:

```text
[1, 3, 2, 4, 5, 6, 7]
```


