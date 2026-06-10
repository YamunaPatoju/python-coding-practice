# Minimum Jumps to Reach End

## Problem Statement

Given an array where each element represents the maximum number of steps that can be jumped forward from that position, find the minimum number of jumps required to reach the end of the array.

If it is not possible to reach the end, return -1.

## Example

**Input:**

[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

**Output:**

3

## Explanation

Jump 1:

Index 0 → Index 1

Jump 2:

Index 1 → Index 4

Jump 3:

Index 4 → End

Minimum jumps = 3

## Approach

Use a Greedy Algorithm.

1. Maintain:

   * maxReach → farthest index reachable.
   * steps → remaining steps in the current jump.
   * jumps → number of jumps taken.
2. Traverse the array.
3. Update maxReach whenever a farther position can be reached.
4. When steps become 0:

   * Take another jump.
   * Update steps.
5. Continue until the end is reached.

