# Merge Two Balanced Binary Search Trees

## Problem

Given two balanced Binary Search Trees (BSTs), merge them into a single balanced BST.

The resulting BST should contain all the elements from both trees and should remain balanced.

If the first tree contains `m` nodes and the second tree contains `n` nodes, the solution should run in **O(m + n)** time.

## Approach

We use the **inorder traversal** property of BSTs.

The inorder traversal of a BST produces its elements in sorted order.

### Steps

1. Perform inorder traversal of the first BST and store the values in `arr1`.
2. Perform inorder traversal of the second BST and store the values in `arr2`.
3. Merge the two sorted arrays into one sorted array.
4. Build a balanced BST from the merged sorted array.
5. Choose the middle element as the root at every step.

## Example

First BST:

```text
        100
       /   \
     50     300
    /  \
   20  70
```

Inorder:

```text
20 50 70 100 300
```

Second BST:

```text
      80
     /  \
    40  120
```

Inorder:

```text
40 80 120
```

Merged sorted array:

```text
20 40 50 70 80 100 120 300
```

A balanced BST can then be constructed from this sorted array.

## Algorithm

```text
inorder(root1) → arr1
inorder(root2) → arr2

merge arr1 and arr2 → merged

buildBalanced(merged):
    choose middle element as root
    build left subtree from left half
    build right subtree from right half
```


