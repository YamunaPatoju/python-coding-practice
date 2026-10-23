# GERGOVIA — Wine Trading in Gergovia

## Problem
Given the buying and selling amounts of inhabitants living along a street, calculate the minimum work required to fulfill everyone's demand.

Positive values represent buyers, and negative values represent sellers. Transporting one bottle of wine across one adjacent house costs one unit of work.

## Approach
Use a greedy approach with a running balance.

The balance represents the amount of wine that must be transported across the current position. The absolute value of this balance gives the work required at that boundary.

## Algorithm
1. Read the number of inhabitants `n`.
2. Stop when `n == 0`.
3. Read the buying and selling amounts.
4. Initialize `balance` and `work` to `0`.
5. Traverse the array:
   - Add the current amount to `balance`.
   - Add `abs(balance)` to `work`.
6. Print the total work.

## Example

**Input:**
```text
5
5 -4 1 -3 1
6
-1000 -1000 -1000 1000 1000 1000
0
```

**Output:**
```text
9
9000
```

