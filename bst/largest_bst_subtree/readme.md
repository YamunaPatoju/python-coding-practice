# Largest BST Subtree

## Problem

Given the root of a binary tree, find the **size of the largest subtree that is also a Binary Search Tree (BST)**.

A subtree is a BST when:

* Every value in the left subtree is smaller than the node.
* Every value in the right subtree is greater than the node.
* There are no duplicate values.

Return the number of nodes in the largest BST subtree.

## Example 1

### Input

```text id="k5v9dr"
[5, 2, 4, 1, 3]
```

### Output

```text id="h3x7mq"
3
```

The subtree rooted at `2` is a BST:

```text id="d6n2qa"
    2
   / \
  1   3
```

So the largest BST has `3` nodes.

## Example 2

### Input

```text id="r4c8yt"
[6, 7, 3, N, 2, 2, 4]
```

### Output

```text id="v2p6ks"
3
```

The largest valid BST subtree contains `3` nodes.

## Approach

Use **postorder traversal**:

```text id="j8q3mz"
Left → Right → Root
```

For every node, calculate four things:

1. Whether the subtree is a BST.
2. Size of the subtree.
3. Minimum value in the subtree.
4. Maximum value in the subtree.

A subtree rooted at `node` is a BST when:

```text id="c7m1px"
left subtree is BST
AND
right subtree is BST
AND
left_max < node.data < right_min
```

If it is a BST, its size is:

```text id="n9v4qw"
left_size + right_size + 1
```

If it is not a BST, we keep the larger BST size from either the left or right subtree.

## Algorithm

```text id="a5k8zr"
1. Recursively process the left subtree.
2. Recursively process the right subtree.
3. Get:
      - BST status
      - size
      - minimum value
      - maximum value
4. Check whether the current subtree is a BST.
5. If it is a BST:
      calculate its size and update min/max.
6. If it is not a BST:
      keep the larger BST size from its children.
7. Return the largest BST size.
```


