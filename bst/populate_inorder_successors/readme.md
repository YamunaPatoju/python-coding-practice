# Populate Inorder Successors

## Problem

Given a binary tree where every node has:

* `left` pointer
* `right` pointer
* `next` pointer

Populate the `next` pointer of every node so that it points to its **inorder successor**.

The node that has no inorder successor does not need to be explicitly assigned `-1`.

## Approach

The inorder traversal of a binary tree follows:

```text
Left → Root → Right
```

During inorder traversal, keep track of the previously visited node.

When we visit the current node:

1. The previous node's inorder successor is the current node.
2. Set `previous.next = current`.
3. Update `previous` to the current node.
4. Continue the traversal.

## Example

### Input

```text
root = [10, 8, 12, 3]
```

Inorder traversal:

```text
3 → 8 → 10 → 12
```

So the `next` pointers become:

```text
3 → 8
8 → 10
10 → 12
12 → -1
```

## Example 2

```text
root = [1, 2, 3]
```

Inorder traversal:

```text
3 → 2 → 1
```

So:

```text
3 → 2
2 → 1
1 → -1
```

## Algorithm

1. Perform inorder traversal.
2. Maintain a `previous` node.
3. For every visited node:

   * If `previous` exists, set `previous.next = current`.
   * Set `previous = current`.
4. The last visited node has no inorder successor.


