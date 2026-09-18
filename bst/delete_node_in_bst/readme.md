# Delete Node in a BST

## Problem

Given the root of a Binary Search Tree (BST) and a key, delete the node with the given key.

Return the root of the updated BST.

## Approach

First, use the BST property to find the node:

* If `key < root.val`, search in the left subtree.
* If `key > root.val`, search in the right subtree.
* If `key == root.val`, the node is found.

There are **3 cases** when deleting a node:

### 1. Node has no children

The node is a leaf, so simply remove it.

### 2. Node has one child

Replace the node with its existing child.

### 3. Node has two children

Find the **inorder successor**, which is the smallest value in the right subtree.

Then:

1. Copy the successor's value into the current node.
2. Delete the successor from the right subtree.

## Example

### Input

```text
root = [5,3,6,2,4,null,7]
key = 3
```

### Output

```text
[5,4,6,2,null,null,7]
```

