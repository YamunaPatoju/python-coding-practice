# Subarray with Zero Sum

## Problem Statement

Given an array of integers, determine whether there exists a subarray whose sum is equal to 0.

Return:

* True if such a subarray exists.
* False otherwise.

## Example 1

**Input:**

[4, 2, -3, 1, 6]

**Output:**

True

**Explanation:**

The subarray [2, -3, 1] has a sum of 0.

## Example 2

**Input:**

[4, 2, 0, 1, 6]

**Output:**

True

**Explanation:**

The element 0 itself forms a subarray with sum 0.

## Example 3

**Input:**

[1, 2, -1]

**Output:**

False

## My Approach

I use the concept of Prefix Sum.

* Keep adding elements and calculate the running sum.
* If the running sum becomes 0, a zero-sum subarray exists.
* If the same running sum appears again, it means the elements between those positions sum to 0.
* Store all prefix sums in a set for quick lookup.

This helps find the answer in a single traversal.

