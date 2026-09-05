# Boundary Traversal of Binary Tree

## Problem

Given the root of a Binary Tree, return its boundary traversal.

The boundary traversal consists of:

1. Left Boundary
2. Leaf Nodes
3. Reverse Right Boundary

The root is included only once, and leaf nodes are excluded from the left and right boundaries because they are added separately.

## Approach

### 1. Add the Root

If the tree contains only one node, that node itself is the answer.

Otherwise, add the root first.

### 2. Left Boundary

Start from the root's left child.

* Add only non-leaf nodes.
* Prefer the left child.
* If the left child does not exist, move to the right child.

### 3. Leaf Nodes

Traverse the complete tree recursively.

* If a node has no left and right child, it is a leaf.
* Add leaf nodes from left to right.

### 4. Reverse Right Boundary

Start from the root's right child.

* Add only non-leaf nodes to a temporary list.
* Prefer the right child.
* If the right child does not exist, move to the left child.
* Reverse the temporary list before adding it to the answer.




