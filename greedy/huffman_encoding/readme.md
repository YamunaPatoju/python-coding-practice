# Huffman Encoding

## Problem

Given a string `s` containing distinct characters and an array `f[]` containing their corresponding frequencies, build the Huffman Tree and return all Huffman codes in preorder traversal.

When two nodes have the same frequency, the node whose subtree contains the character appearing earlier in `s` must be placed on the left.

## Approach

Huffman Encoding uses a **Greedy** approach with a **Min Heap**.

1. Create a node for every character with its frequency.
2. Store all nodes in a min heap.
3. Remove the two nodes with the smallest frequencies.
4. Make a new internal node with the sum of their frequencies.
5. Put the first node on the left and the second node on the right.
6. Use the original character index as a tie-breaker when frequencies are equal.
7. Insert the new node back into the heap.
8. Repeat until only one node remains.
9. Traverse the final tree:

   * Left edge → `0`
   * Right edge → `1`
10. Store the code whenever a leaf node is reached.

## Algorithm

```text
Create a min heap containing all characters.

While more than one node exists:
    Remove the two minimum nodes.
    Create a new node with their combined frequency.
    Make the first node the left child.
    Make the second node the right child.
    Insert the new node into the heap.

Traverse the Huffman Tree:
    Left  → 0
    Right → 1

Store the code of every leaf node.
Return the codes.
```

## Example

### Input

```text
s = "abcdef"
f = [5, 9, 12, 13, 16, 45]
```

### Output

```text
[0, 100, 101, 1100, 1101, 111]
```

The Huffman codes are:

```text
f → 0
c → 100
d → 101
a → 1100
b → 1101
e → 111
```


