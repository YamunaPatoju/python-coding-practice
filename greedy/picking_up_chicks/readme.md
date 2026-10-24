# GCJ101BB — Picking Up Chicks

## Problem
Given the initial positions and speeds of `N` chicks, determine the minimum number of adjacent swaps required so that at least `K` chicks reach the barn at position `B` within time `T`.

A chick can reach the barn if its distance to the barn is no greater than the distance it can travel in time `T`. Slower chicks can block faster chicks behind them.

## Approach
Use a greedy approach by traversing the chicks from right to left.

- If a chick can reach the barn on its own, count it as a successful chick.
- Every slower chick that cannot reach the barn independently must be passed by a successful chick, requiring one swap.
- Add the number of slower chicks to the swap count whenever a successful chick is found.
- Stop once `K` successful chicks have been counted.

## Algorithm
1. Read the number of test cases.
2. For each test case, read `N`, `K`, `B`, `T`, the positions, and the speeds.
3. If `K == 0`, output `0`.
4. Traverse the chicks from right to left.
5. Check whether each chick can reach the barn using `V[i] * T >= B - X[i]`.
6. If it can reach, count it and add the number of slower chicks encountered to the swap count.
7. If it cannot reach, increment the slower-chick count.
8. If fewer than `K` chicks can reach, output `IMPOSSIBLE`; otherwise, output the minimum swaps.

## Example

**Input:**
```text
3
5 3 10 5
0 2 5 6 7
1 1 1 1 4
5 3 10 5
0 2 3 5 7
2 1 1 1 4
5 3 10 5
0 2 3 4 7
2 1 1 1 4
```

**Output:**
```text
Case #1: 0
Case #2: 2
Case #3: IMPOSSIBLE
```


