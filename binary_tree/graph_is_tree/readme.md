# Graph is Tree or Not

## Problem

Given an undirected graph with `n` nodes and `m` edges, determine whether the graph is a tree.

The graph can contain:

* Self-loops
* Multiple edges between the same pair of nodes

A graph is a tree if:

1. It has exactly `n - 1` edges.
2. It is connected.
3. It contains no cycle.

## Approach

First, check the number of edges.

A tree with `n` nodes must have exactly:

```text
n - 1
```

edges.

If this condition is not satisfied, return `False`.

Then build an adjacency list and use BFS.

During BFS, store the parent of every node. If we find a visited neighbor that is not the parent, a cycle exists.

Finally, check whether all `n` nodes were visited.

## Example

Input:

```text
n = 4
m = 3
edges = [[0, 1], [1, 2], [2, 3]]
```

Graph:

```text
0 --- 1 --- 2 --- 3
```

There are `3 = 4 - 1` edges, the graph is connected, and there is no cycle.

Output:

```text
True
```

## Why Check `m = n - 1`?

For an undirected graph to be a tree, it must have exactly `n - 1` edges.

For example:

```text
n = 4

Required edges = 4 - 1 = 3
```

If there are more edges, a cycle must exist.

If there are fewer edges, the graph cannot be connected.

## Handling Self-Loops

Example:

```text
edges = [[0, 0]]
```

A self-loop creates a cycle, so the graph is not a tree.

The BFS detects this because node `0` sees itself as an already visited neighbor that is not its parent.

## Handling Multiple Edges

Example:

```text
edges = [[0, 1], [0, 1]]
```

There are two edges between the same nodes, which creates a cycle in an undirected graph.

The BFS detects the second connection as a visited neighbor that is not the parent.

