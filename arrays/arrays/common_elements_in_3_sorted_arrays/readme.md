# Common Elements in 3 Sorted Arrays

## Problem Statement

Given three sorted arrays, find all elements that are present in all three arrays.

Duplicate elements should be included only once in the output.

## Example

**Input:**

a = [1, 5, 10, 20, 40, 80]

b = [6, 7, 20, 80, 100]

c = [3, 4, 15, 20, 30, 70, 80, 120]

**Output:**

[20, 80]

## My Approach

Since all three arrays are already sorted, I used three pointers.

* One pointer for each array.
* If all three elements are equal, add the element to the result.
* Otherwise, move the pointer having the smallest value.
* To avoid duplicates, check the last element added to the result.

This helps find common elements efficiently without checking every possible combination.

