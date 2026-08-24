# Delete Nodes with Greater Value on Right

## Problem Statement

Given a singly linked list, delete every node that has a node with a greater value somewhere to its right.

Return the head of the modified linked list.

## Example

### Input

```text
12 -> 15 -> 10 -> 11 -> 5 -> 6 -> 2 -> 3
```

### Output

```text
15 -> 11 -> 6 -> 3
```

## Approach

Use a stack to process the linked list from left to right.

- Store nodes in the stack.
- When the current node has a greater value than the node at the top of the stack, remove the smaller node.
- Continue removing smaller nodes until the top of the stack is greater than or equal to the current node.
- Add the current node to the stack.
- Reconnect the remaining nodes at the end.

## Algorithm

1. Create an empty stack.
2. Traverse the linked list.
3. For every current node:
   - Remove nodes from the stack while their value is smaller than the current node.
   - Add the current node to the stack.
4. Reconnect all nodes remaining in the stack.
5. Set the last node's `next` to `None`.
6. Return the first node in the stack.

