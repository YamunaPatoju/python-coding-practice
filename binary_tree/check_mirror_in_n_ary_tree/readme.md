# Check Mirror in N-ary Tree

## Problem

Given two n-ary trees represented using their edges, check whether they are mirror images of each other.

Each pair `(u, v)` represents an edge from node `u` to node `v`.

## Approach

* Create an adjacency list for both trees.
* Store the children of each node in the given order.
* For two trees to be mirror images, the children of every node in the second tree must be in the reverse order of the children in the first tree.
* Compare the child lists of both trees.
* If every list matches in reverse order, return `True`.
* Otherwise, return `False`.

## Example

### Input

```text
e = 2
t1 = [1, 2, 1, 3]
t2 = [1, 3, 1, 2]
```

The children of node `1` are:

```text
Tree 1 → [2, 3]
Tree 2 → [3, 2]
```

The order is reversed, so the trees are mirror images.

### Output

```text
True
```

## Another Example

```text
e = 2
t1 = [1, 2, 1, 3]
t2 = [1, 2, 1, 3]
```

The children are in the same order instead of reverse order.

### Output

```text
False
```


