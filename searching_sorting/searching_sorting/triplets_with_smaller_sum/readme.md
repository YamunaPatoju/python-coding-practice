# Triplets with Smaller Sum

## Problem Statement

Given an array `arr[]` of distinct integers and an integer `sum`, count the number of triplets `(i, j, k)` such that:

- `i < j < k`
- `arr[i] + arr[j] + arr[k] < sum`

Return the total number of such triplets.

---

## Example 1

**Input**

```text
arr = [-2, 0, 1, 3]
sum = 2
```

**Output**

```text
2
```

**Explanation**

Valid triplets:

```text
(-2, 0, 1)
(-2, 0, 3)
```

---

## Example 2

**Input**

```text
arr = [5, 1, 3, 4, 7]
sum = 12
```

**Output**

```text
4
```

**Explanation**

Valid triplets are:

```text
(1, 3, 4)
(5, 1, 3)
(5, 1, 4)
(1, 3, 7)
```

---

## Approach

Use **Sorting + Two Pointers**.

1. Sort the array.
2. Fix the first element.
3. Use two pointers to find the remaining two elements.
4. If the current triplet sum is less than the target, then all elements between `left` and `right` also form valid triplets.

Instead of checking each one individually:

```text
count += (right - left)
```

This reduces the time complexity from `O(n³)` to `O(n²)`.

---

## Algorithm

1. Sort the array.
2. Traverse the array with index `i`.
3. Initialize:
   - `left = i + 1`
   - `right = n - 1`
4. Calculate:

```text
current_sum = arr[i] + arr[left] + arr[right]
```

- If `current_sum < sum`
  - Add `(right - left)` to the answer.
  - Move `left` forward.
- Otherwise
  - Move `right` backward.
5. Continue until all triplets are checked.
6. Return the count.

---

