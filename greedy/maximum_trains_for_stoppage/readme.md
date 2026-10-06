# Maximum Trains for Which Stoppage Can Be Provided

## Problem

Given `n` trains and `m` platforms, each train is represented by:

* `trains[i][0]` → arrival time
* `trains[i][1]` → departure time
* `trains[i][2]` → platform number

A platform can handle only one stopping train at a time.

If one train departs at time `T` and another train arrives at the same time `T`, the platform can be reused.

Find the maximum number of trains that can be given stoppage without conflicts.

## Approach

Use a **Greedy** approach.

Each platform can be handled independently.

For every platform:

1. Collect all trains assigned to that platform.
2. Sort the trains by departure time.
3. Select the train that departs earliest.
4. For each following train, select it if its arrival time is greater than or equal to the previous selected train's departure time.
5. Add the selected trains to the total count.

## Algorithm

```text id="7p3x4m"
Group trains according to their platform.

For each platform:
    Sort trains by departure time.

    last_departure = -1

    For every train:
        If arrival >= last_departure:
            Select the train.
            Increase count.
            Update last_departure.

Return count.
```

## Example 1

### Input

```text id="q6w2na"
m = 2

trains = [
    [1000, 1030, 1],
    [1101, 1130, 1],
    [1101, 1130, 2]
]
```

### Output

```text id="k8v4cz"
3
```

Both trains on platform 1 can be scheduled, and the train on platform 2 can also be scheduled.


