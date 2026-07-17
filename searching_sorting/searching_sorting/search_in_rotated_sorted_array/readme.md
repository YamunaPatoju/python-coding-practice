# Search in Rotated Sorted Array

## Problem Statement

Given a sorted array that has been rotated at an unknown pivot and a target value, return the index of the target if it exists in the array. Otherwise, return `-1`.

The solution must run in **O(log n)** time.

---

## Example 1

**Input**

```text
nums = [4,5,6,7,0,1,2]
target = 0
```

**Output**

```text
4
```

---

## Example 2

**Input**

```text
nums = [4,5,6,7,0,1,2]
target = 3
```

**Output**

```text
-1
```

---

## Example 3

**Input**

```text
nums = [1]
target = 0
```

**Output**

```text
-1
```

---

## Approach

Use a modified **Binary Search**.

At every iteration:

- Find the middle element.
- Check whether the **left half** is sorted or the **right half** is sorted.
- Determine whether the target lies in the sorted half.
- Search only in the appropriate half.

This reduces the search space by half every time.

---

## Algorithm

1. Initialize `low = 0` and `high = n - 1`.
2. While `low <= high`:
   - Find `mid`.
   - If `nums[mid] == target`, return `mid`.
   - If the left half is sorted:
     - If the target lies in the left half, move `high`.
     - Otherwise, move `low`.
   - Else, the right half is sorted:
     - If the target lies in the right half, move `low`.
     - Otherwise, move `high`.
3. If the target is not found, return `-1`.

---

