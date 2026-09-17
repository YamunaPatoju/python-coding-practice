# Search in BST

## Problem

Given a Binary Search Tree (BST) and a value `key`, check whether a node with the value `key` exists in the BST.

Return `True` if the key is present, otherwise return `False`.

## Approach

A Binary Search Tree follows this rule:

* Values smaller than the current node are in the **left subtree**.
* Values greater than the current node are in the **right subtree**.

So, instead of searching every node:

1. Start from the root.
2. If the current node is `None`, return `False`.
3. If the current node's value equals `key`, return `True`.
4. If `key` is smaller, search the left subtree.
5. If `key` is greater, search the right subtree.

## Example

### Input

```text
root = [6, 2, 8, N, N, 7, 9]
key = 8
```

### Output

```text
True
```


