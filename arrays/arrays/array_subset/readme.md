# Array Subset

## Problem Statement

Given two arrays `a` and `b`, determine whether `b` is a subset of `a`.

A subset means every element of `b` must be present in `a` with the required frequency.

## Example 1

**Input:**

a = [11, 7, 1, 13, 21, 3, 7, 3]

b = [11, 3, 7, 1, 7]

**Output:**

True

## Example 2

**Input:**

a = [10, 5, 2, 23, 19]

b = [19, 5, 3]

**Output:**

False

## Example 3

**Input:**

a = [2, 2]

b = [2, 2, 2]

**Output:**

False

**Explanation:**

Array `a` contains only two occurrences of 2, but array `b` requires three occurrences.

## My Approach

I use a frequency dictionary to count how many times each element appears in array `a`.

Then I traverse array `b`:

* If an element is not present in the frequency dictionary, return False.
* If its count becomes zero before all occurrences are matched, return False.
* Otherwise, decrease its count and continue.

If all elements of `b` are matched successfully, return True.

