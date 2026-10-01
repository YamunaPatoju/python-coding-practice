# Activity Selection

## Topic

**Greedy Algorithm**

## Problem

Given two arrays `start[]` and `finish[]`, where:

* `start[i]` is the starting time of activity `i`.
* `finish[i]` is the finishing time of activity `i`.

Find the **maximum number of activities** that a single person can perform.

A person can perform only one activity at a time.

If one activity finishes at time `x`, the next activity must start at a time **greater than `x`**.

## Example

### Input

```text id="k3v8qp"
start  = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
```

### Output

```text id="x7m2qa"
4
```

One possible selection is:

```text id="n5c9rz"
(1,2) → (3,4) → (5,7) → (8,9)
```

So, `4` activities can be performed.

## Greedy Approach

The main idea is:

> **Always choose the activity that finishes earliest.**

Why?

An activity that finishes earlier leaves more time for other activities.

So:

1. Combine the start and finish times.
2. Sort all activities by their finish time.
3. Select the first activity.
4. For every next activity:

   * Select it only if its start time is greater than the finish time of the previously selected activity.
5. Count the selected activities.

## Algorithm

```text id="q8r4mv"
1. Create pairs of (start, finish).
2. Sort activities according to finish time.
3. Set count = 0.
4. Set last_finish = -1.
5. Traverse the sorted activities:
      If start > last_finish:
          Select the activity.
          Increase count.
          Update last_finish.
6. Return count.
```
