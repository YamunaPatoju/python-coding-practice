# Replace with Least Greater on Right

## Problem

Given an array `arr[]`, replace every element with the **least greater element on its right side**.

If there is no greater element on the right, replace it with `-1`.

## Example

### Input

```text id="j9y5cs"
arr = [86, 53, 80, 26, 66, 70]
```

For each element:

* `86` → no greater element on the right → `-1`
* `53` → least greater is `66`
* `80` → no greater element on the right → `-1`
* `26` → least greater is `66`
* `66` → least greater is `70`
* `70` → no greater element on the right → `-1`

### Output

```text id="q2y7hr"
[-1, 66, -1, 66, 70, -1]
```

## Approach

Process the array from **right to left**.

For every element, maintain the elements already seen on its right in a Binary Search Tree.

The BST helps us find the **successor** of the current element.

The successor is the smallest value that is strictly greater than the current value.

### Steps

1. Start from the last element.
2. Find the smallest BST value greater than the current element.
3. Store that value as the answer.
4. Insert the current element into the BST.
5. Continue towards the beginning of the array.


