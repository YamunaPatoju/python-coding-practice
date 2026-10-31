# Min Cost to Connect Ropes

## Problem
Given an array of rope lengths, connect all ropes into a single rope with the minimum possible total cost.

The cost of connecting two ropes is the sum of their lengths.

## Approach – Greedy + Min Heap
- Convert the array into a min heap.
- Remove the two smallest ropes.
- Connect them and calculate their combined cost.
- Add the connection cost to the total cost.
- Insert the newly connected rope back into the heap.
- Repeat until only one rope remains.

## Example

**Input:** `[4, 3, 2, 6]`

**Output:** `29`

Connection steps:
- Connect 2 + 3 = 5
- Connect 4 + 5 = 9
- Connect 6 + 9 = 15

Total cost = 5 + 9 + 15 = 29

