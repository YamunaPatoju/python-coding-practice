# Smallest Number with D Digits and Sum S

## Problem
Given two integers `s` and `d`, find the smallest `d`-digit number whose digits add up to `s`.

Return the number as a string. If no valid number exists, return `"-1"`.

## Approach – Greedy
- Check whether the required sum is possible. If `s > 9 * d`, return `"-1"`.
- Reserve 1 for the first digit because the number must have exactly `d` digits.
- Fill the remaining digits from right to left, placing as much of the remaining sum as possible in each position (maximum 9).
- Add the reserved 1 to the first digit.
- Convert the digits into a string and return it.

## Example

**Input:** `s = 20, d = 3`

**Output:** `"299"`



