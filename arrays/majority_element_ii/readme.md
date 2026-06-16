# Majority Element II

## Problem Statement

Given an integer array, find all elements that appear more than ⌊n/3⌋ times.

Return the elements in a list.

## Example 1

**Input:**

[3, 2, 3]

**Output:**

[3]

## Example 2

**Input:**

[1]

**Output:**

[1]

## Example 3

**Input:**

[1, 2]

**Output:**

[1, 2]

## My Approach

I first remove duplicate elements using a set.

For each unique element:

* Count how many times it appears in the array.
* If its count is greater than n/3, add it to the result.

Finally, return the result list.

This approach is simple and easy to understand.

