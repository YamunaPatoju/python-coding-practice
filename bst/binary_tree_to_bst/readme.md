# Binary Tree to BST

## Problem

Given a Binary Tree, convert it into a **Binary Search Tree (BST)** while keeping the original structure of the Binary Tree unchanged.

Only the values of the nodes should be changed.

## Approach

The important idea is:

* The structure of the tree must remain the same.
* A BST's inorder traversal is always sorted.

So we can use two inorder traversals.

### Step 1: Store all values

Perform an inorder traversal of the original binary tree and store all node values in an array.

### Step 2: Sort the values

Sort the collected values in ascending order.

### Step 3: Replace node values

Perform inorder traversal again and assign the sorted values to the nodes.

Because the structure remains unchanged and the values are assigned in sorted inorder order, the resulting tree becomes a BST.

## Example

Suppose the original tree contains:

```text
        10
       /  \
      2    7
```

Inorder traversal:

```text
2 → 10 → 7
```

Sorted values:

```text
2 → 7 → 10
```

Assigning them back using inorder traversal gives:

```text
        7
       / \
      2   10
```

The structure is unchanged, but the tree is now a BST.

## Algorithm

1. Perform inorder traversal and store all node values.
2. Sort the values.
3. Perform inorder traversal again.
4. Replace each node's value with the next sorted value.
5. Return the root.

