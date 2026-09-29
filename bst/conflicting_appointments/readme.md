# Conflicting Appointments

## Problem

Given `n` appointments represented as intervals, find all appointments that conflict with any of the previous appointments.

Two appointments conflict when their time intervals overlap.

### Example

Input:

```text
[[1,5], [3,7], [2,6], [10,15], [5,6], [4,100]]
```

Output:

```text
[3,7] Conflicts with [1,5]
[2,6] Conflicts with [1,5]
[5,6] Conflicts with [3,7]
[4,100] Conflicts with [1,5]
```

## Approach

We use an **Interval Tree**.

Each node stores:

* The appointment interval.
* The maximum ending time of all intervals in its subtree.
* Left and right child pointers.

For every new appointment:

1. Search the interval tree for an overlapping appointment.
2. If an overlap is found, print the conflict.
3. Insert the current appointment into the interval tree.

## Overlap Condition

Two intervals `[a,b]` and `[c,d]` overlap when:

```text
a < d and c < b
```

For example:

```text
[1,5] and [3,7]
```

overlap because:

```text
1 < 7
3 < 5
```

## Algorithm

```text
1. Create an empty interval tree.
2. Insert the first appointment.
3. For every remaining appointment:
   a. Search the tree for an overlapping interval.
   b. If found, report the conflict.
   c. Insert the appointment into the tree.
4. Continue until all appointments are processed.
```


