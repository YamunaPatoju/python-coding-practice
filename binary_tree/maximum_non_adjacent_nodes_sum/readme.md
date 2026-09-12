# Maximum Non-Adjacent Nodes Sum

## Problem

Given a binary tree, find the maximum possible sum of nodes such that no two selected nodes are directly connected.

If a node is selected, its parent and children cannot be selected.

## Approach

Use **Dynamic Programming on the Tree**.

For every node, calculate two values:

* `include` → maximum sum when the current node is selected.
* `exclude` → maximum sum when the current node is not selected.

### If the current node is included

Its children cannot be included.

```text
include = node.data + left_exclude + right_exclude
```

### If the current node is excluded

We can either include or exclude each child.

```text
exclude = max(left_include, left_exclude)
        + max(right_include, right_exclude)
```

Finally, return the maximum of `include` and `exclude` for the root.

## Example

Input:

```text
        1
       / \
      2   3
     /   / \
    4   5   6
```

The optimal selection is:

```text
1 + 4 + 5 + 6 = 16
```

Output:

```text
16
```
