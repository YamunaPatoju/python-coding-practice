# Pair Sum in Sorted Doubly Linked List

## Problem

Given a sorted doubly linked list containing distinct integers and an integer `target`, find all pairs of nodes whose values add up to `target`.

## Approach

Use the two-pointer technique:

- `left` starts at the head.
- `right` starts at the last node.
- If the sum equals the target, store the pair and move both pointers.
- If the sum is smaller than the target, move `left` forward.
- If the sum is greater than the target, move `right` backward.
- Stop when the pointers meet or cross.

## Example

### Input

```text
List: 0 2 3 4 5 6 7 8 9 10
Target: 8
