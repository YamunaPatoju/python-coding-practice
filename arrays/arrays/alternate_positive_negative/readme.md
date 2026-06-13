# Alternate Positive Negative

## Problem Statement

Given an array containing both positive and negative numbers, rearrange the array so that positive and negative numbers appear alternately.

Rules:

* The resulting array should start with a positive number.
* Maintain the relative order of positive numbers.
* Maintain the relative order of negative numbers.
* If one type of number is exhausted, append the remaining elements as they are.

## Example

**Input:**

[9, 4, -2, -1, 5, 0, -5, -3, 2]

**Output:**

[9, -2, 4, -1, 5, -5, 0, -3, 2]

## My Approach

I first separate all positive and negative numbers into two different lists.

* Store positive numbers in one list.
* Store negative numbers in another list.
* Add elements alternately from both lists.
* If one list becomes empty, add the remaining elements from the other list.

This maintains the original order of elements.

