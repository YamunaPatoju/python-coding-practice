# Find the Duplicate Number

## Problem Statement

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]`, find and return the duplicate number.

## Example 1

**Input:**

[1, 3, 4, 2, 2]

**Output:**

2

## Example 2

**Input:**

[3, 1, 3, 4, 2]

**Output:**

3

## Example 3

**Input:**

[3, 3, 3, 3, 3]

**Output:**

3

## Approach

1. Create an empty set called `seen`.
2. Traverse the array.
3. If the current element is already present in the set, it is the duplicate number.
4. Return the duplicate number.
5. Otherwise, add the element to the set and continue.


