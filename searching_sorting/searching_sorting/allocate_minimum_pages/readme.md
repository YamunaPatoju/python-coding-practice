# Allocate Minimum Pages

## Problem Statement

Given an array `arr[]` where each element represents the number of pages in a book and an integer `k` representing the number of students, allocate books such that:

- Each student gets at least one book.
- Books assigned to a student are contiguous.
- Every book is allocated exactly once.
- The maximum pages assigned to any student is minimized.

If allocation is impossible, return `-1`.

---

## Example 1

**Input**

```text
arr = [12, 34, 67, 90]
k = 2
```

**Output**

```text
113
```

**Explanation**

Optimal allocation:

```text
[12, 34, 67] | [90]
```

Maximum pages assigned = **113**.

---

## Example 2

**Input**

```text
arr = [15, 17, 20]
k = 5
```

**Output**

```text
-1
```

Since there are more students than books, allocation is impossible.

---

## Approach

Use **Binary Search on the Answer**.

The minimum possible maximum pages is:

```text
max(arr)
```

The maximum possible maximum pages is:

```text
sum(arr)
```

Binary search this range.

For each candidate value:

- Check whether all books can be allocated using at most `k` students.
- If yes, try a smaller value.
- Otherwise, increase the limit.

---

## Algorithm

1. If `k > number of books`, return `-1`.
2. Set:
   - `low = max(arr)`
   - `high = sum(arr)`
3. Perform Binary Search.
4. For each `mid`, greedily allocate books.
5. If allocation is possible:
   - Search left half.
6. Else:
   - Search right half.
7. Return the minimum feasible value.

---

