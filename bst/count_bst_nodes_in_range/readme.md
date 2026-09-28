# Count BST Nodes in Range

## Problem

Given a Binary Search Tree (BST) and a range `[l, h]`, count the number of nodes whose values lie within the range **inclusively**.

A node is counted if:

```text
l <= node.data <= h
```

## Approach

We use the BST property to avoid visiting unnecessary subtrees.

### Cases

* If `node.data < l`, then the current node and its entire left subtree are smaller than the range. We only search the **right subtree**.
* If `node.data > h`, then the current node and its entire right subtree are larger than the range. We only search the **left subtree**.
* Otherwise, the node lies inside the range, so we count it and search both subtrees.

## Algorithm

```text
1. If root is None, return 0.
2. If root.data < l:
      Search only the right subtree.
3. If root.data > h:
      Search only the left subtree.
4. Otherwise:
      Count the current node.
      Search both left and right subtrees.
5. Return the total count.
```

## Example 1

### Input

```text
root = [10, 5, 50, 1, N, 40, 100]
l = 5
h = 45
```

Nodes in the range `[5, 45]` are:

```text
5, 10, 40
```

### Output

```text
3
```

## Example 2

### Input

```text
root = [10, 5, 50, 1, N, 40, 100]
l = 10
h = 100
```

Nodes in the range `[10, 100]` are:

```text
10, 40, 50, 100
```

### Output

```text
4
```

