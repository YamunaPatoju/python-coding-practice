# Minimum Platforms

## Problem

Given the arrival times `arr[]` and departure times `dep[]` of trains on the same day, find the minimum number of platforms required so that no train has to wait.

A platform cannot serve two trains at the same time.

If a train arrives before or at the same time another train departs, an additional platform is required.

## Approach

Use a **Greedy + Two Pointer** approach.

1. Sort all arrival times.
2. Sort all departure times.
3. Use two pointers:

   * `i` for arrivals
   * `j` for departures
4. If the next train arrives before or at the next departure:

   * We need another platform.
5. Otherwise:

   * A train has departed, so one platform becomes free.
6. Keep track of the maximum number of platforms used at any time.

## Algorithm

```text
Sort arr[]
Sort dep[]

i = 0
j = 0
platforms = 0
answer = 0

While i < n and j < n:

    If arr[i] <= dep[j]:
        A train arrives.
        platforms += 1
        update answer
        i += 1

    Else:
        A train departs.
        platforms -= 1
        j += 1

Return answer
```

## Example 1

### Input

```text
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
```

After sorting:

```text
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1120, 1130, 1200, 1900, 2000]
```

Between `950` and `1120`, three trains are present.

Therefore:

```text
Output = 3
```

