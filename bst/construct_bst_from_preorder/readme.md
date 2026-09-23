# Construct Binary Search Tree from Preorder Traversal

## Problem

Given an array `preorder` representing the preorder traversal of a Binary Search Tree (BST), construct the BST and return its root.

Preorder traversal visits nodes in this order:

```text
Root → Left → Right
```

## Approach

We use the BST property together with the preorder traversal.

For every node:

* Values smaller than the node belong to the left subtree.
* Values greater than the node belong to the right subtree.

We maintain an `index` pointing to the next value in the preorder array.

For each recursive call:

1. Check whether the current value is within the allowed range.
2. Create a node.
3. Build its left subtree using values smaller than the node.
4. Build its right subtree using values greater than the node.

## Example

### Input

```text
preorder = [8, 5, 1, 7, 10, 12]
```

### Constructed BST

```text
        8
       / \
      5   10
     / \    \
    1   7    12
```

### Output

```text
[8,5,10,1,7,null,12]
```

## Example 2

### Input

```text
preorder = [1, 3]
```

### Output

```text
[1,null,3]
```

Since `3 > 1`, it becomes the right child of `1`.

## Algorithm

1. Start with the first preorder element.
2. Maintain an allowed range for each subtree.
3. If the current value is outside the range, do not consume it.
4. Create the node and move the index forward.
5. Recursively construct the left subtree.
6. Recursively construct the right subtree.
7. Return the root.

## Complexity

* **Time:** O(n)
* **Space:** O(h), where `h` is the height of the constructed BST.

For a skewed BST, the recursion depth can be O(n).
For a balanced BST, it is approximately O(log n).
