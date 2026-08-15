# Count Triplets in a Sorted Doubly Linked List

## Problem

Given a sorted doubly linked list of distinct nodes and an integer `x`, count the number of triplets whose sum is equal to `x`.

## Approach

Use the two-pointer technique for each fixed first node.

- Fix the first node.
- Set the second pointer to `first.next`.
- Set the third pointer to the last node.
- Calculate the sum of the three values.
- If the sum equals `x`, increment the count and move both pointers.
- If the sum is smaller than `x`, move the second pointer forward.
- If the sum is greater than `x`, move the third pointer backward.
- Repeat for every possible first node.

## Example

### Input

```text
Doubly Linked List: 1 2 4 5 6 8 9
x = 17
