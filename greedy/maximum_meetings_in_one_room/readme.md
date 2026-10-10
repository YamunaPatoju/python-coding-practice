# Maximum Meetings in One Room

## Problem

Given two arrays `s[]` and `f[]`, representing the start and finish times of meetings, find the maximum number of non-overlapping meetings that can be scheduled in a single room.

A meeting can be selected only if its start time is **strictly greater** than the finish time of the previously selected meeting.

Return the selected meeting indices in increasing order using 1-based indexing.

If multiple schedules are possible, prefer meetings with earlier finish times. If finish times are equal, prefer the meeting with the smaller index.

## Approach

Use a **Greedy** approach.

- Store each meeting's finish time, index, and start time.
- Sort meetings by finish time, then by index.
- Select a meeting if its start time is strictly greater than the last selected meeting's finish time.
- Return the selected indices in increasing order.

## Algorithm

1. Create tuples `(finish, index, start)` for all meetings.
2. Sort the tuples in ascending order.
3. Initialize `last_finish = -1`.
4. Iterate through the sorted meetings:
   - If `start > last_finish`, select the meeting.
   - Update `last_finish` to the current finish time.
5. Sort the selected indices and return them.

## Example

### Input

```text
s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
```

### Output

```text
[1, 2, 4, 5]
```

### Explanation

The selected meetings are:

- Meeting 1: `(1, 2)`
- Meeting 2: `(3, 4)`
- Meeting 4: `(5, 7)`
- Meeting 5: `(8, 9)`

Each meeting starts strictly after the previous meeting finishes.

