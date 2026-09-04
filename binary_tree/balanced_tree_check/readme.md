# Balanced Tree Check

## Problem

Given the root of a binary tree, determine whether the tree is **height-balanced**.

A binary tree is height-balanced if the absolute difference between the heights of the left and right subtrees of **every node** is at most `1`.

## Approach

Use a recursive DFS approach.

For every node:

1. Find the height of the left subtree.
2. Find the height of the right subtree.
3. If either subtree is already unbalanced, return `-1`.
4. If the height difference is greater than `1`, return `-1`.
5. Otherwise, return the height of the current subtree.

Finally, if the returned value is not `-1`, the tree is balanced.

## Complexity

* **Time:** `O(n)`
* **Space:** `O(h)`

Where:

* `n` = number of nodes
* `h` = height of the binary tree

## Example

### Input

```text
        10
       /  \
      20   30
     / \
    40  60
```

### Output

```text
True
```


