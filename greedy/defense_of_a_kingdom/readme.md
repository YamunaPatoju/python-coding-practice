# DEFKIN — Defense of a Kingdom

## Problem
Given a rectangular grid of width `w` and height `h`, some cells contain crossbow towers. Each tower defends its entire row and column.

Find the number of cells in the largest rectangle that is not defended by any tower.

## Approach
Use a greedy approach by finding the largest consecutive gap between tower coordinates along both dimensions.

Add boundary positions `0`, `w + 1` for columns and `0`, `h + 1` for rows. Sort the coordinates and calculate the largest number of empty columns and rows between consecutive positions.

The largest undefended rectangle is the product of these two maximum gaps.

## Algorithm
1. Read the number of test cases.
2. For each test case, read `w`, `h`, and `n`.
3. Initialize coordinate lists with the boundary positions.
4. Read all tower coordinates and add them to the corresponding lists.
5. Sort both coordinate lists.
6. Find the maximum empty gap between consecutive column coordinates.
7. Find the maximum empty gap between consecutive row coordinates.
8. Multiply the two maximum gaps and print the result.

## Example

**Input:**
```text
1
15 8 3
3 8
11 2
8 6
```

**Output:**
```text
12
```

