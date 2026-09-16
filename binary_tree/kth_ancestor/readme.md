# Kth Ancestor of a Node in Binary Tree

## Problem

Given a binary tree, a node, and a positive integer `K`, find the **Kth ancestor** of the given node.

If the Kth ancestor does not exist, return `-1`.

An ancestor is a node that occurs on the path from the given node towards the root.

## Example

Consider the binary tree:

```text
        1
       / \
      2   3
     / \
    4   5
```

For:

```text
node = 5
k = 2
```

The ancestors of `5` are:

```text
5 → 2 → 1
```

So:

* 1st ancestor = `2`
* 2nd ancestor = `1`

Output:

```text
1
```

If `k = 3`, there is no such ancestor.

Output:

```text
-1
```

## Approach

Use **Depth First Search (DFS)**.

The main idea is:

1. Search for the target node recursively.
2. Once the target is found, return `True` while backtracking.
3. Every node encountered during backtracking is an ancestor.
4. Decrease `k` for each ancestor.
5. When `k` becomes `0`, the current node is the Kth ancestor.
6. Store its value.
7. If no Kth ancestor is found, return `-1`.

