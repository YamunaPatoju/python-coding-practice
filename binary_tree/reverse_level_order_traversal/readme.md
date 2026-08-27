# Reverse Level Order Traversal

## Problem Statement

Given a binary tree, find its reverse level order traversal.

The traversal starts from the last level of the binary tree and moves upward to the root. Nodes within the same level are visited from left to right.

## Examples

### Example 1

**Input:**

```text
1
/ \
3   2
```

**Output:**

```text
[3, 2, 1]
```

### Example 2

**Input:**

```text
10
/  \
20   30
/ \
40  60
```

**Output:**

```text
[40, 60, 20, 30, 10]
```

## Approach

- Use a queue to perform level order traversal.
- Process the binary tree level by level.
- Store each level separately.
- Insert each completed level at the beginning of the result.
- Keep nodes within each level in left-to-right order.
- Flatten the levels to get the final reverse level order traversal.

## Algorithm

1. If `root` is `None`, return an empty list.
2. Create a queue and add the root node.
3. While the queue is not empty:
   - Create a list for the current level.
   - Process all nodes of the current level.
   - Add each node's data to the level list.
   - Add the left and right children to the queue.
   - Insert the level at the beginning of the result.
4. Flatten the result.
5. Return the final list.

