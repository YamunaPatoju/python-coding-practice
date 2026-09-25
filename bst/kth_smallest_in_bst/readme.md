# K-th Smallest in BST

## Problem

Given the root of a Binary Search Tree (BST) and an integer `k`, find the **k-th smallest element** in the BST.

If the k-th smallest element does not exist, return `-1`.

## Approach

In a BST, inorder traversal visits the nodes in **ascending order**:

```text
Left → Root → Right
```

Therefore, the k-th node visited during inorder traversal is the **k-th smallest element**.

We decrease `k` every time we visit a node.

When `k` becomes `0`, the current node contains the required answer.

## Algorithm

```text
1. Start inorder traversal from the root.
2. Traverse the left subtree.
3. Visit the current node.
4. Decrease k by 1.
5. If k becomes 0, store the current node's value.
6. Traverse the right subtree.
7. If no node makes k equal to 0, return -1.
```

## Example 1

### Input

```text
root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14]
k = 3
```

Inorder traversal:

```text
4 → 8 → 10 → 12 → 14 → 20 → 22
```

The 3rd smallest element is:

```text
10
```

### Output

```text
10
```

## Example 2

### Input

```text
root = [2, 1, 3]
k = 5
```

Inorder traversal:

```text
1 → 2 → 3
```

There are only 3 nodes, so the 5th smallest element does not exist.

### Output

```text
-1
```



