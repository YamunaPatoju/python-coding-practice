# Longest Consecutive Subsequence

## Problem Statement

Given an array of integers, find the length of the longest subsequence containing consecutive integers.

The consecutive numbers can appear in any order in the array.

## Example 1

**Input:**

[2, 6, 1, 9, 4, 5, 3]

**Output:**

6

**Explanation:**

The consecutive numbers are:

1, 2, 3, 4, 5, 6

Length = 6

## Example 2

**Input:**

[1, 9, 3, 10, 4, 20, 2]

**Output:**

4

**Explanation:**

The consecutive numbers are:

1, 2, 3, 4

Length = 4

## Example 3

**Input:**

[15, 13, 12, 14, 11, 10, 9]

**Output:**

7

**Explanation:**

The consecutive numbers are:

9, 10, 11, 12, 13, 14, 15

Length = 7

## My Approach

I first store all elements in a set.

For each number:

* Check if it is the starting element of a sequence.
* A number is considered a starting point if `num - 1` is not present in the set.
* From that number, keep checking for the next consecutive numbers.
* Count the length of the sequence.
* Update the longest length found so far.

Using a set makes searching very fast.


