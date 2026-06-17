# Triplet Sum in Array

## Problem Statement

Given an array and a target value, determine whether there exists a triplet whose sum is equal to the target.

Return:

* True if such a triplet exists.
* False otherwise.

## Example 1

**Input:**

arr = [1, 4, 45, 6, 10, 8]

target = 13

**Output:**

True

**Explanation:**

The triplet [1, 4, 8] has a sum of 13.

## Example 2

**Input:**

arr = [1, 2, 4, 3, 6, 7]

target = 10

**Output:**

True

**Explanation:**

Possible triplets:

[1, 3, 6]

[1, 2, 7]

## Example 3

**Input:**

arr = [40, 20, 10, 3, 6, 7]

target = 24

**Output:**

False

## My Approach

I first sort the array.

Then for every element:

* Fix it as the first element of the triplet.
* Use two pointers to find the remaining two elements.
* If the sum is smaller than the target, move the left pointer.
* If the sum is larger than the target, move the right pointer.
* If the sum equals the target, return True.

If no triplet is found, return False.

