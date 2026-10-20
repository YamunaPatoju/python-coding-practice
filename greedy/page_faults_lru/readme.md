# Page Faults in LRU

## Problem
Given a sequence of page requests and a memory capacity `C`, calculate the total number of page faults using the **Least Recently Used (LRU)** page replacement algorithm.

A page fault occurs when the requested page is not present in memory. If memory is full, the least recently used page is removed.

## Approach
Use Python's `OrderedDict` to maintain pages in order of recent usage.

- If a page is already in memory, move it to the most recently used position.
- If a page is not in memory, increment the page fault count.
- If memory is full, remove the least recently used page.
- Insert the new page into memory.

## Algorithm
1. Initialize an empty ordered dictionary and set page faults to `0`.
2. Traverse each page in the request sequence.
3. If the page exists in memory, mark it as most recently used.
4. Otherwise, increment the fault count.
5. If memory is full, remove the least recently used page.
6. Insert the requested page.
7. Return the total page faults.

## Example

**Input:**
- Capacity: `4`
- Pages: `[5, 0, 1, 3, 2, 4, 1, 0, 5]`

**Output:**
`8`


