# Dead End in BST

## Problem

Given a Binary Search Tree containing unique positive integers, determine whether the BST contains a **dead end**.

A dead end is a leaf node where no new positive integer can be inserted while maintaining the BST property.

Return `True` if a dead end exists, otherwise return `False`.

## Example 1

### Input

```text id="y4m8kd"
[8, 5, 9, 2, 7, N, N, 1]
```

### Output

```text id="z6n2px"
True
```

Node `1` is a dead end because its valid range contains only `1`.

The value `0` is not allowed because all node values must be positive.

## Example 2

### Input

```text id="p5v7qa"
[61, 23, N, 1]
```

### Output

```text id="r8c3wx"
False
```

Node `1` is a leaf, but it is **not** a dead end.

Its valid range is:

```text
1 to 22
```

So values such as `2`, `3`, ..., `22` can still be inserted.

## Approach

Instead of checking only `node.data - 1` and `node.data + 1`, we maintain the **valid range** of values that can be inserted at every position.

For each node:

* Left subtree contains values from `low` to `node.data - 1`.
* Right subtree contains values from `node.data + 1` to `high`.

A leaf is a dead end when:

```text id="w7j3pd"
low == high
```

This means there is only one possible value in that position, and that value is already occupied by the leaf.

## Algorithm

```text id="f4q9zn"
1. Start with the range [1, 100000].
2. Traverse the BST recursively.
3. For a node:
   - Left subtree gets [low, node.data - 1].
   - Right subtree gets [node.data + 1, high].
4. When a leaf is reached:
   - If low == high, it is a dead end.
   - Otherwise, another value can still be inserted.
5. Return True if any dead end is found.
6. Otherwise return False.
```


