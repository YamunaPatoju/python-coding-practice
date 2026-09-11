# Sum of Nodes on the Longest Path

## Problem

Given a binary tree, find the sum of nodes on the longest path from the root to any leaf.

If there are multiple paths with the same length, return the maximum sum among those paths.

## Approach

Use Depth First Search (DFS) to visit every root-to-leaf path.

For each path, keep track of:

* `length` - number of nodes in the current path
* `total` - sum of nodes in the current path
* `maxLen` - length of the longest path found
* `maxSum` - maximum sum for the longest path

When a leaf node is reached:

1. If the current path is longer than the previous longest path, update `maxLen` and `maxSum`.
2. If the current path has the same length, keep the larger sum.

## Example

```text
        4
       / \
      2   5
     / \
    7   1
       /
      6
```

The longest path is:

```text
4 -> 2 -> 1 -> 6
```

Sum:

```text
4 + 2 + 1 + 6 = 13
```

Output:

```text
13
```

