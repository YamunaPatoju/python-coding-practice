# Minimum Swaps Required to Convert Binary Tree to Binary Search Tree

## Problem

Given an array representing a **Complete Binary Tree**, find the minimum number of swaps required to convert it into a **Binary Search Tree (BST)**.

For an array representation:

* Left child of index `i` → `2 * i + 1`
* Right child of index `i` → `2 * i + 2`

## Key Idea

The important property of a BST is:

> **Inorder traversal of a BST is sorted in increasing order.**

Therefore:

1. Perform inorder traversal of the given binary tree.
2. Store the inorder traversal in an array.
3. Sort the inorder array.
4. Find the minimum number of swaps required to transform the original inorder array into the sorted array.

The minimum swaps can be calculated using **cycle detection**.

## Example

### Input

```text
arr = [5, 6, 7, 8, 9, 10, 11]
```

The inorder traversal is:

```text
[8, 6, 9, 5, 10, 7, 11]
```

To make the tree a BST, the inorder traversal should be sorted:

```text
[5, 6, 7, 8, 9, 10, 11]
```

The minimum number of swaps required is:

```text
3
```

### Output

```text
3
```

## Algorithm

### Step 1: Inorder Traversal

For an array-based complete binary tree:

```text
Left  → 2*i + 1
Root  → i
Right → 2*i + 2
```

Perform inorder traversal and store the values.

### Step 2: Sort the Inorder Array

Create pairs containing:

```text
(value, original_index)
```

Then sort the pairs by value.

### Step 3: Detect Cycles

The sorted array tells us where every element should go.

For a cycle containing `k` elements:

```text
minimum swaps = k - 1
```

Add the swaps for all cycles.


