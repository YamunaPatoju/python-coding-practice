# Smallest Subset with Greater Sum

## Problem
Given an array of positive integers, find the minimum number of elements required so that their sum is greater than the sum of all remaining elements.

## Approach
Use a greedy approach by sorting the array in descending order. Select the largest elements first because they help the selected sum exceed the remaining sum using fewer elements.

## Algorithm
1. Sort the array in descending order.
2. Calculate the total sum of the array.
3. Initialize the selected sum to `0`.
4. Traverse the sorted array:
   - Add the current element to the selected sum.
   - Subtract it from the remaining sum.
   - If the selected sum becomes greater than the remaining sum, return the number of selected elements.
5. Return the array length if necessary.

## Example

**Input:** `[2, 17, 7, 3]`

**Output:** `1`

