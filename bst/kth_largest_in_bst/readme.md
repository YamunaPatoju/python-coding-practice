# Kth Largest in BST

## Problem

Given the root of a Binary Search Tree (BST) and an integer `k`, find the **k-th largest element** in the BST without modifying its structure.

## Approach

In a BST, normal inorder traversal visits nodes in ascending order:

```text
Left → Root → Right
```

To get elements from largest to smallest, we use **reverse inorder traversal**:

```text
Right → Root → Left
```

Every time we visit a node, we decrease `k`.

When `k` becomes `0`, the current node is the k-th largest element.

## Algorithm

```text
1. Start from the root.
2. Traverse the right subtree first.
3. Visit the current node.
4. Decrease k by 1.
5. If k becomes 0, return the current node's value.
6. Traverse the left subtree.
```

## Example

### Input

```text
root = [4, 2, 9]
k = 2
```

Reverse inorder traversal:

```text
9 → 4 → 2
```

The 2nd largest element is:

```text
4
```

### Output

```text
4
```


