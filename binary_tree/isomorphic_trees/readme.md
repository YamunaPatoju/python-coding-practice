# Isomorphic Trees

## Problem

Given two binary trees with roots `root1` and `root2`, check whether the two trees are **isomorphic**.

Two binary trees are isomorphic if one tree can be obtained from the other by swapping the left and right children of any number of nodes.

The children of each node can be swapped independently.

## Approach

Use **recursive DFS** to compare both trees.

For every pair of corresponding nodes:

1. If both nodes are `None`, they are isomorphic.
2. If only one node is `None`, they are not isomorphic.
3. If their values are different, they are not isomorphic.
4. Check two possibilities:

   * **Without swapping:** left matches left and right matches right.
   * **With swapping:** left matches right and right matches left.
5. If either possibility is true, the two subtrees are isomorphic.

## Example

Input:

```text
root1 = [1, 2, 3, 4]
root2 = [1, 3, 2, 4]
```

The children of node `1` can be swapped, but node `4` cannot be matched correctly.

Output:

```text
false
```

## Another Example

Input:

```text
root1 = [1, 2, 3, 4]
root2 = [1, 3, 2, N, N, N, 4]
```

Swapping the left and right children of node `1` makes the trees structurally identical.

Output:

```text
true
```

## Algorithm

```text
isIsomorphic(root1, root2)

    If both nodes are None:
        return True

    If one node is None:
        return False

    If values are different:
        return False

    Check without swapping:
        left  → left
        right → right

    Check with swapping:
        left  → right
        right → left

    Return True if either case is True
```

