# In-Place Merge Sort

## Problem Statement

Implement Merge Sort without using an extra temporary array during the merge operation.

Unlike standard Merge Sort, the merge should be performed **in-place**, meaning no additional array is used for merging.

---

## Example 1

### Input

```text
[2, 3, 4, 1]
```

### Output

```text
[1, 2, 3, 4]
```

---

## Example 2

### Input

```text
[56, 2, 45]
```

### Output

```text
[2, 45, 56]
```

---

## Approach

Normal Merge Sort requires an extra temporary array.

In the in-place version:

- Compare the first elements of both sorted halves.
- If they are already in order, move forward.
- Otherwise:
  - Store the smaller element.
  - Shift all elements between the two positions by one step.
  - Insert the stored element into its correct position.

No extra merge array is used.

---

## Algorithm

1. Divide the array into two halves.
2. Recursively sort both halves.
3. Merge them in-place:
   - Compare current elements.
   - If needed, shift elements to insert the smaller value.
4. Continue until the whole array is sorted.

---

