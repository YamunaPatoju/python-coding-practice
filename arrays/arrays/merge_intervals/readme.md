# Merge Intervals

## Problem Statement

Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals and return an array of the non-overlapping intervals.

## Example 1

**Input:**

[[1,3],[2,6],[8,10],[15,18]]

**Output:**

[[1,6],[8,10],[15,18]]

## Example 2

**Input:**

[[1,4],[4,5]]

**Output:**

[[1,5]]

## Approach

1. Sort the intervals based on their start time.
2. Add the first interval to the result list.
3. Traverse the remaining intervals.
4. If the current interval overlaps with the last merged interval:

   * Update the ending value of the merged interval.
5. Otherwise:

   * Add the current interval to the result list.
6. Return the merged intervals.

