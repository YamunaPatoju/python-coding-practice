# Sort a Linked List of 0s, 1s and 2s

## Problem Statement

Given the head of a linked list containing only `0`, `1`, and `2`, rearrange the list so that all `0`s come first, followed by all `1`s, and then all `2`s.

## Example

### Input

```text
1 -> 2 -> 2 -> 1 -> 2 -> 0 -> 2 -> 2
```

### Output

```text
0 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 2
```

## Approach

- Traverse the linked list once and count the number of `0`s, `1`s, and `2`s.
- Traverse the linked list again.
- Replace the node values using the stored counts.
- First fill all nodes with `0`.
- Then fill all nodes with `1`.
- Finally fill all nodes with `2`.
- Return the original head.

## Algorithm

1. Create a count array of size `3`.
2. Traverse the linked list and increment the count corresponding to each node's data.
3. Traverse the list again.
4. For each value from `0` to `2`:
   - Replace the current node's data with that value.
   - Continue until all occurrences of that value are placed.
5. Return `head`.


