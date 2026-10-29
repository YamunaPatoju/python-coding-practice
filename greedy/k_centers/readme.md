# K Centers Problem

## Problem
Given a distance matrix representing distances between cities and an integer `k`, select exactly `k` cities to place ATMs. Minimize the maximum distance from any city to its nearest ATM.

## Approach
- Generate all possible subsets of cities using bitmasks.
- Consider only subsets containing exactly `k` cities.
- For each city, find the distance to its nearest selected ATM.
- Calculate the maximum of these nearest distances.
- Return the minimum maximum distance among all valid subsets.

