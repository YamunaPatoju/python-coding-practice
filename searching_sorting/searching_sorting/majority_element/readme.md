# Majority Element

## Problem Statement

Given an array `arr[]`, find the **majority element**.

A majority element is an element that appears **more than n/2 times**, where `n` is the size of the array.

If no majority element exists, return `-1`.

---

## Example 1

**Input**

```text
arr = [1, 1, 2, 1, 3, 5, 1]
```

**Output**

```text
1
```

**Explanation**

`1` appears 4 times, and:

```text
4 > 7/2
```

So, `1` is the majority element.

---

## Example 2

**Input**

```text
arr = [7]
```

**Output**

```text
7
```

---

## Example 3

**Input**

```text
arr = [2, 13]
```

**Output**

```text
-1
```

---

## Approach

Use the **Boyer-Moore Voting Algorithm**.

### Phase 1

Find a candidate for the majority element by maintaining:

- `candidate`
- `count`

### Phase 2

Verify whether the candidate actually appears more than `n/2` times.

---

## Algorithm

1. Initialize `candidate = None` and `count = 0`.
2. Traverse the array:
   - If `count == 0`, choose the current element as the candidate.
   - If the current element equals the candidate, increment `count`.
   - Otherwise, decrement `count`.
3. Count the occurrences of the candidate.
4. If its frequency is greater than `n/2`, return it.
5. Otherwise, return `-1`.

---

