# Two Sum - Pairs with Zero Sum

## Problem Statement

Given an array of integers, find all unique pairs whose sum is equal to 0.

A pair should be included only once in the output.

## Example

**Input:**

[-1, 0, 1, 2, -1, -4]

**Output:**

[[-1, 1]]

## My Approach

I used two nested loops to check every possible pair in the array.

* If the sum of two elements is 0, a valid pair is found.
* Before adding the pair to the result, I check whether it already exists to avoid duplicates.
* Finally, I sort the result and return it.

This approach is simple and easy to understand.

