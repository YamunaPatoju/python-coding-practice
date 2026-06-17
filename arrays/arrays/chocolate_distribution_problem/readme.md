# Chocolate Distribution Problem

## Problem Statement

Given an array where each element represents the number of chocolates in a packet and `m` students, distribute exactly one packet to each student.

The goal is to minimize the difference between the maximum and minimum chocolates received by the students.

Return the minimum possible difference.

## Example 1

**Input:**

arr = [3, 4, 1, 9, 56, 7, 9, 12]

m = 5

**Output:**

6

**Explanation:**

Selected packets:

[3, 4, 7, 9, 9]

Difference:

9 - 3 = 6

## Example 2

**Input:**

arr = [7, 3, 2, 4, 9, 12, 56]

m = 3

**Output:**

2

**Explanation:**

Selected packets:

[2, 3, 4]

Difference:

4 - 2 = 2

## My Approach

First, sort the array.

After sorting:

* Any group of `m` packets will be consecutive.
* Calculate the difference between the first and last packet in each group.
* Keep track of the minimum difference.

The smallest difference obtained is the answer.

