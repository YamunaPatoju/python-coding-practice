# Predecessor and Successor in BST

## Problem

Given a Binary Search Tree (BST) and an integer `key`, find:

* **Inorder predecessor:** Largest value smaller than `key`.
* **Inorder successor:** Smallest value greater than `key`.

If the predecessor or successor does not exist, return `NULL`.

The key may or may not be present in the BST.

## Approach

We search the BST while keeping track of possible predecessor and successor.

### If `current.data < key`

The current node can be a predecessor because it is smaller than the key.

Move to the **right subtree** to find a larger value that is still smaller than the key.

### If `current.data > key`

The current node can be a successor because it is greater than the key.

Move to the **left subtree** to find a smaller value that is still greater than the key.

### If `current.data == key`

The node is found.

* Predecessor is the **rightmost node of the left subtree**.
* Successor is the **leftmost node of the right subtree**.

## Example

### Input

```text
root = [50, 30, 70, 20, 40, 60, 80]
key = 65
```

### Output

```text
[60, 70]
```

### Explanation

For `65`:

* `60` is the largest value smaller than `65`.
* `70` is the smallest value greater than `65`.

Therefore:

```text
Predecessor = 60
Successor = 70
```

## Example 2

```text
root = [8, 1, 9, N, 4, N, 10, 3]
key = 8
```

Output:

```text
[4, 9]
```

