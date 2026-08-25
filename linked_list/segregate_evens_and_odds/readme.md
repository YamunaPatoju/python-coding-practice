# Segregate Evens and Odds in a Linked List

## Problem Statement

Given the head of a singly linked list, rearrange the list so that all nodes containing even values appear before the nodes containing odd values.

The relative order of the even nodes and the odd nodes should remain unchanged.

## Example

### Input

```text
7 -> 8 -> 9 -> 1 -> 2 -> 1 -> 6
```

### Output

```text
8 -> 2 -> 6 -> 7 -> 9 -> 1 -> 1
```

## Approach

- Maintain two separate linked lists: one for even nodes and one for odd nodes.
- Traverse the original linked list.
- Add each node to the corresponding even or odd list.
- Preserve the original order while adding nodes.
- Connect the even list to the odd list.
- Return the head of the even list.

## Algorithm

1. Initialize `even_head`, `even_tail`, `odd_head`, and `odd_tail` as `None`.
2. Traverse the linked list.
3. If the current node contains an even value, add it to the even list.
4. Otherwise, add it to the odd list.
5. If there are no even nodes, return the odd list.
6. Connect `even_tail` to `odd_head`.
7. Return `even_head`.

