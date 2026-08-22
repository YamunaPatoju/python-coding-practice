# Clone List with Next and Random

## Problem Statement

Given a linked list where every node has a `next` pointer and a `random` pointer, create a deep copy of the linked list.

The copied list must:

- Have the same number of nodes.
- Have the same node values.
- Preserve the `next` relationships.
- Preserve the `random` relationships.
- Contain completely new nodes.
- Not contain any pointer to a node from the original list.
- Leave the original linked list unchanged.

## Example

### Input

```text
[[1, 3], [3, 3], [5, NULL], [9, 3]]
```

### Output

```text
[[1, 3], [3, 3], [5, NULL], [9, 3]]
```

## Approach

Use the **interleaving technique**.

Instead of using a dictionary to map original nodes to copied nodes, insert every copied node immediately after its original node.

For example:

```text
Original:

A -> B -> C

After inserting copies:

A -> A' -> B -> B' -> C -> C'
```

This makes it possible to assign random pointers without using extra space.

## Algorithm

1. If `head` is `None`, return `None`.

2. Traverse the original list.
   - Create a copy of every node.
   - Insert the copied node immediately after the original node.

3. Traverse the interleaved list.
   - If the original node has a random pointer:
     - The copied node's random pointer can be found using `curr.random.next`.

4. Separate the original and copied lists.
   - Restore the original list.
   - Construct the cloned list.

5. Return the head of the cloned list.

