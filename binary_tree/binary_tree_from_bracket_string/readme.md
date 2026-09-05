# Binary Tree from Bracket String

## Problem

Given a string representing a binary tree, construct the binary tree and return its root.

The string contains:

* An integer representing the current node.
* A pair of parentheses representing the left subtree.
* A second pair of parentheses representing the right subtree.

For a right-only child, an empty pair of parentheses `()` represents the missing left child.

## Examples

### Example 1

```text
Input:
"1(2)(3)"

Tree:

    1
   / \
  2   3

Inorder:
2 1 3
```

### Example 2

```text
Input:
"4(2(3)(1))(6(5))"

Tree:

        4
       / \
      2   6
     / \  /
    3   1 5

Inorder:
3 2 1 4 5 6
```

### Example 3

```text
Input:
"1()(3)"

Tree:

    1
     \
      3

Inorder:
1 3
```

## Approach

Use recursion to parse the string.

For every node:

1. Read all digits to construct the node value.
2. If the next character is `(`, process the first bracket as the left subtree.
3. If the next character is another `(`, process it as the right subtree.
4. An empty bracket `()` represents a missing child.
5. Return the constructed node and the current index.

### Parsing Example

For:

```text
"4(2(3)(1))(6(5))"
```

We first create:

```text
4
```

Then parse the first bracket:

```text
(2(3)(1))
```

which becomes the left subtree.

Then parse:

```text
(6(5))
```

which becomes the right subtree.

Final tree:

```text
        4
       / \
      2   6
     / \  /
    3   1 5
```

## Why an Index Is Used

Instead of creating new substrings repeatedly, maintain an index `i` pointing to the current position in the original string.

The recursive function returns:

```text
(node, next_index)
```

This avoids repeatedly slicing the string and is important because the input can contain up to `10^6` characters.




