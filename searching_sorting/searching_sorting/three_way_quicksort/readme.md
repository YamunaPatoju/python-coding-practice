# Three-Way QuickSort (Dutch National Flag Algorithm)

## Problem Statement

Standard QuickSort performs poorly when the array contains many duplicate elements.

Three-Way QuickSort improves the partition process by dividing the array into three parts:

- Elements smaller than the pivot
- Elements equal to the pivot
- Elements greater than the pivot

This greatly improves performance for arrays with many repeated values.

---

## Example

### Input

```text
[4, 9, 4, 4, 2, 7, 4, 1]
```

### Output

```text
[1, 2, 4, 4, 4, 4, 7, 9]
```

---

## Approach

Choose the first element as the pivot.

Maintain three pointers:

- **lt** → boundary of elements smaller than pivot
- **i** → current element
- **gt** → boundary of elements greater than pivot

Process every element:

- If current element is smaller than pivot, swap with `lt`
- If equal, move forward
- If greater, swap with `gt`

After partitioning:

- Recursively sort the left part.
- Recursively sort the right part.
- No need to sort the middle part because all values are equal.

---

## Algorithm

1. Choose first element as pivot.
2. Initialize:
   - lt = left
   - i = left
   - gt = right
3. While i ≤ gt:
   - If arr[i] < pivot:
     - swap(arr[lt], arr[i])
     - lt++
     - i++
   - Else if arr[i] > pivot:
     - swap(arr[i], arr[gt])
     - gt--
   - Else:
     - i++
4. Recursively sort:
   - left part
   - right part

---

