# SUBSUMS - Subset Sums

## Problem Statement

Given `N` numbers (`N ≤ 34`), count how many subsets have a sum in the range:

```text
A ≤ Sum ≤ B
```

The empty subset is also included.

---

## Example

### Input

```text
3 -1 2
1
-2
3
```

### Output

```text id="8p5fne"
5
```

---

## Why Normal Backtracking Fails

For:

```text id="4kt0b1"
N = 34
```

Total subsets:

```text id="1wq8m3"
2^34 ≈ 17 billion
```

This is impossible to generate directly.

---

## Meet in the Middle

Split the array into two halves:

```text id="onf69v"
Left half
Right half
```

Generate all subset sums:

```text id="7f6f0s"
2^(17) ≈ 131072
```

for each side.

Then:

- Sort right sums.
- For each left sum:
  - Use Binary Search to count valid right sums.

---

## Algorithm

1. Split array into two halves.
2. Generate all subset sums for both halves.
3. Sort right-half sums.
4. For every left sum:
   - Find valid range:
   
```text id="v04g5g"
A - leftSum
B - leftSum
```

5. Use:
   - `bisect_left()`
   - `bisect_right()`

6. Add count to answer.

---

