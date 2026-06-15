# Maximum Product Subarray

## Problem Statement

Given an array containing positive numbers, negative numbers, and zeros, find the maximum product that can be obtained from any contiguous subarray.

## Example 1

**Input:**

[-2, 6, -3, -10, 0, 2]

**Output:**

180

**Explanation:**

The subarray [6, -3, -10] gives the maximum product.

6 × (-3) × (-10) = 180

## Example 2

**Input:**

[-1, -3, -10, 0, 6]

**Output:**

30

**Explanation:**

The subarray [-3, -10] gives the maximum product.

## Example 3

**Input:**

[2, 3, 4]

**Output:**

24

## My Approach

For sums, we only track the maximum value.

For products, negative numbers can change everything:

* A large positive product can become negative.
* A large negative product can become positive.

So I keep track of:

* Maximum product ending at the current position.
* Minimum product ending at the current position.

Whenever a negative number appears, I swap them because multiplying by a negative reverses their roles.

Finally, I keep updating the overall maximum product.

