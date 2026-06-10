# Minimize the Maximum Difference Between Heights

## Problem Statement

Given an array representing the heights of towers and an integer k, increase or decrease each tower height by k exactly once. Find the minimum possible difference between the highest and lowest towers after modification.

## Example

**Input:**

arr = [1, 5, 8, 10]

k = 2

**Output:**

5

## Explanation

Modified heights:

[3, 3, 6, 8]

Maximum Height = 8

Minimum Height = 3

Difference = 5

## Approach

1. Sort the array.
2. Calculate the initial difference between the tallest and shortest tower.
3. Increase the smallest tower by k.
4. Decrease the largest tower by k.
5. Traverse the array and calculate the new minimum and maximum heights.
6. Update the minimum difference obtained.

