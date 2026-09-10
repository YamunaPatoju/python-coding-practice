# Duplicate Subtree Check

## Problem

Given the root of a binary tree, check whether the tree contains any duplicate subtree of size two or more.

Two subtrees are considered duplicates if they have the same structure and identical node values.

A subtree containing only a single leaf node is not considered a duplicate subtree.

## Approach

* Traverse the tree using DFS.
* Create a unique representation for every subtree using:

  * Current node value
  * Left subtree representation
  * Right subtree representation
* Store these subtree representations in a set.
* If the same representation appears again, a duplicate subtree exists.
* Single leaf nodes are ignored because their left and right subtrees are both empty.

## Example

```text
        1
       / \
      2   3
         / \
        2   4
           / \
          4   5
```


