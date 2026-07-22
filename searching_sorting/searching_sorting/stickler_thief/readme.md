# Stickler Thief

## Problem Statement

Stickler the thief wants to steal money from houses arranged in a straight line.

He **cannot rob two consecutive houses**.

Given an array `arr[]`, where `arr[i]` represents the money in the `i-th` house, find the **maximum amount of money** that can be looted.

---

## Example 1

**Input**

```text
arr = [6, 7, 1, 3, 8, 2, 4]
```

**Output**

```text
19
```

**Explanation**

Rob houses:

```text
6 + 1 + 8 + 4 = 19
```

---

## Example 2

**Input**

```text
arr = [5, 3, 4, 11, 2]
```

**Output**

```text
16
```

**Explanation**

Rob houses:

```text
5 + 11 = 16
```

---

## Approach

This is a classic **Dynamic Programming** problem.

For every house, there are two choices:

1. **Rob the current house**
   - Add its money to the best value excluding the previous house.

2. **Skip the current house**
   - Keep the previous maximum loot.

Transition:

```text
current = max(previous, previous2 + currentHouse)
```

Where:

- `previous` = maximum loot till the previous house.
- `previous2` = maximum loot till two houses before.

---

## Algorithm

1. Initialize:

```text
prev2 = 0
prev1 = 0
```

2. Traverse every house.
3. Compute:

```text
curr = max(prev1, prev2 + money)
```

4. Update:

```text
prev2 = prev1
prev1 = curr
```

5. Return `prev1`.

---

