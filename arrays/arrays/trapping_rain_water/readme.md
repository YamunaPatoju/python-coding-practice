# Trapping Rain Water

## Problem Statement

Given an array where each element represents the height of a block, find the total amount of rain water that can be trapped between the blocks.

Each block has a width of 1 unit.

## Example 1

**Input:**

[3, 0, 1, 0, 4, 0, 2]

**Output:**

10

## Example 2

**Input:**

[3, 0, 2, 0, 4]

**Output:**

7

## Example 3

**Input:**

[1, 2, 3, 4]

**Output:**

0

## My Approach

For every block, the amount of water stored depends on:

* The tallest block on its left.
* The tallest block on its right.

Water stored at an index:

Water = min(Left Maximum, Right Maximum) - Current Height

Steps:

1. Create a left maximum array.
2. Create a right maximum array.
3. For every position, calculate trapped water.
4. Add all trapped water values.

