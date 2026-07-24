# Zero Sum Subarrays

## Problem Statement

Given an integer array `arr[]`, count the total number of **subarrays whose sum is equal to 0**.

---

## Example 1

**Input**

```text
arr = [0, 0, 5, 5, 0, 0]
```

**Output**

```text
6
```

**Explanation**

Zero-sum subarrays are:

```text
[0]
[0]
[0]
[0]
[0,0]
[0,0]
```

---

## Example 2

**Input**

```text
arr = [6, -1, -3, 4, -2, 2, 4, 6, -12, -7]
```

**Output**

```text
4
```

---

## Example 3

**Input**

```text
arr = [0]
```

**Output**

```text
1
```

---

## Approach

Use **Prefix Sum + Hash Map**.

### Key Observation

If two prefix sums are equal, then the sum of the elements between them is **0**.

Maintain:

- `prefix_sum` → running sum
- `freq` → frequency of each prefix sum

Initially:

```text
freq = {0:1}
```

This handles subarrays starting from index `0`.

---

## Algorithm

1. Initialize:
   - `prefix_sum = 0`
   - `count = 0`
   - `freq = {0:1}`
2. Traverse the array.
3. Add the current element to `prefix_sum`.
4. If `prefix_sum` already exists in the map:
   - Add its frequency to the answer.
5. Increase the frequency of the current prefix sum.
6. Return the count.

---

