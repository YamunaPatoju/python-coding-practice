# Chocolate Distribution Problem

## Problem
Given an array where each element represents the number of chocolates in a packet, distribute exactly one packet to each of `m` students such that the difference between the maximum and minimum chocolates is minimized.

## Approach
Use sorting and a sliding window of size `m`. After sorting, packets with the smallest difference will appear in a group of `m` consecutive elements.

## Algorithm
1. If `m == 1`, return `0` because only one student receives a packet.
2. Sort the array in ascending order.
3. Initialize the minimum difference to infinity.
4. Traverse every group of `m` consecutive packets.
5. Calculate the difference between the last and first elements of each group.
6. Update the minimum difference.
7. Return the minimum difference.

## Example

**Input:** `arr = [3, 4, 1, 9, 56, 7, 9, 12]`, `m = 5`

**Output:** `6`


