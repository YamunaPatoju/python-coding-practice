# Median of BST

## Problem

Given the root of a Binary Search Tree (BST), find the **median** of the BST.

The nodes of the BST are considered in ascending order using inorder traversal.

If the number of nodes is:

* **Odd:** Return `V((n + 1) / 2)`
* **Even:** Return `V(n / 2)`

Here, `V` represents the sorted inorder sequence.

## Approach

Inorder traversal of a BST gives all values in **ascending order**.

So we:

1. Perform inorder traversal.
2. Store all node values in a list.
3. Find the total number of nodes.
4. If `n` is odd, return the middle element.
5. If `n` is even, return the left-middle element as required by the problem.

## Algorithm

```text
1. Perform inorder traversal of the BST.
2. Store node values in a list.
3. Let n = number of nodes.
4. If n is odd:
      return values[n // 2]
5. Otherwise:
      return values[(n // 2) - 1]
```

## Example 1

### Input

```text
root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14]
```

Inorder traversal:

```text
4, 8, 10, 12, 14, 20, 22
```

There are `7` nodes.

Since `7` is odd, the median is the 4th value:

```text
12
```

### Output

```text
12
```

## Example 2

### Input

```text
root = [5, 4, 8, 1]
```

Inorder traversal:

```text
1, 4, 5, 8
```

There are `4` nodes.

Since `4` is even, the problem asks for the 2nd value:

```text
4
```

### Output

```text
4
```


