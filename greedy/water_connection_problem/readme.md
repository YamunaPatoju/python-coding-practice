# Water Connection Problem

## Problem

There are `n` houses and `p` pipes.

Each pipe is represented by:

* `a[i]` → starting house
* `b[i]` → ending house
* `d[i]` → pipe diameter

Each house has at most:

* One outgoing pipe
* One incoming pipe

A house with an outgoing pipe but no incoming pipe is the **tank** (start of a chain).

A house with an incoming pipe but no outgoing pipe is the **tap** (end of a chain).

For every chain, find:

* Tank house
* Tap house
* Minimum pipe diameter in the chain

Return the results sorted by tank number.

## Approach

Use two structures:

1. `outgoing` stores the pipe leaving each house.
2. `incoming` stores all houses that have an incoming pipe.

A tank is a house that:

```text
has an outgoing pipe
AND
does not have an incoming pipe
```

Starting from every tank, follow the chain until there is no outgoing pipe.

While traversing the chain, keep track of the minimum pipe diameter.

## Algorithm

```text
Store every outgoing pipe:
    outgoing[a] = (b, diameter)

Store every house that has an incoming pipe.

For every house from 1 to n:
    If it has an outgoing pipe
    and does not have an incoming pipe:

        This house is a tank.

        Start following the chain.

        Set minimum diameter = infinity.

        While there is an outgoing pipe:
            Move to the next house.
            Update minimum diameter.

        The final house is the tap.

        Add [tank, tap, minimum diameter].
```

## Example

### Input

```text
n = 9
p = 6

a = [7, 5, 4, 2, 9, 3]
b = [4, 9, 6, 8, 7, 1]
d = [98, 72, 10, 22, 17, 66]
```

### Chains

```text
3 → 1
5 → 9 → 7 → 4 → 6
2 → 8
```

### Output

```text
[[2, 8, 22], [3, 1, 66], [5, 6, 10]]
```

For the chain:

```text
5 → 9 → 7 → 4 → 6
```

the pipe diameters are:

```text
72, 17, 98, 10
```

Therefore:

```text
minimum = 10
```

