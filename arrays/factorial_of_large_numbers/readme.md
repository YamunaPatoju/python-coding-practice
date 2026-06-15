# Factorials of Large Numbers

## Problem Statement

Given an integer `n`, find its factorial and return the digits of the factorial as a list.

A factorial is calculated as:

n! = 1 × 2 × 3 × ... × n

## Example 1

**Input:**

5

**Output:**

[1, 2, 0]

**Explanation:**

5! = 120

## Example 2

**Input:**

10

**Output:**

[3, 6, 2, 8, 8, 0, 0]

**Explanation:**

10! = 3628800

## Example 3

**Input:**

1

**Output:**

[1]

## My Approach

I first calculate the factorial using a loop.

After getting the factorial value:

* Convert it into a string.
* Traverse each character.
* Convert each digit back to an integer.
* Store the digits in a list.

Since Python can handle very large integers, this solution is simple and works efficiently.
