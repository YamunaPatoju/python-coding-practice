# Flatten BST to Sorted List

## Problem

Given the root of a Binary Search Tree (BST), flatten it into a **right-skewed tree** such that:

* The left child of every node is `NULL`.
* The right child points to the next node in **inorder traversal**.
* The inorder sequence is preserved.
* All original nodes must be present.

## Example

### Input

```text
[5, 3, 7, 2, 4, 6, 8]
```

The BST is:

```text
        5
       / \
      3   7
     / \ / \
    2  4 6  8
```

### Output

```text
[2, N, 3, N, 4, N, 5, N, 6, N, 7, N, 8]
```

The flattened tree becomes:

```text
2
 \
  3
   \
    4
     \
      5
       \
        6
         \
          7
           \
            8
```

## Approach

A BST's **inorder traversal** gives its values in sorted order.

So:

1. Perform inorder traversal.
2. Store the nodes themselves in a list.
3. Set the left child of every node to `None`.
4. Connect every node's right child to the next node in the list.
5. Return the first node.

## Algorithm

```text
1. Perform inorder traversal of the BST.
2. Store every node in a list.
3. For each node:
      Set left = NULL.
      Set right = next node.
4. Set the last node's right = NULL.
5. Return the first node.
```


