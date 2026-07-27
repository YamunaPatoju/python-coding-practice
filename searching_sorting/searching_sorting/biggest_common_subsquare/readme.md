# Biggest Common Subsquare (BCS)

## Problem Statement

You are given two matrices:

- Matrix **A** of size `n × m`
- Matrix **B** of size `x × y`

A **Square** is a matrix having the same number of rows and columns.

A **Subsquare** is a square submatrix obtained by selecting consecutive rows and consecutive columns.

Your task is to find the **largest common square submatrix** present in both matrices and print its size.

---

## Example

### Input

```text
A =
1 2 0
1 2 1
1 2 3

B =
0 1 2
1 1 2
3 1 2
```

### Output

```text
2
```

---

## Approach

A brute-force solution would compare every possible square submatrix of both matrices.

This would take:

```text
O((NM)(XY)L²)
```

which is far too slow for matrices of size up to **700 × 700**.

Instead, use:

- **Binary Search** on the answer (square size).
- **2D Rolling Hash** to efficiently compare square submatrices.

### Steps

1. Binary search the possible square size.
2. Compute hashes of all square submatrices of size `k` in matrix **A**.
3. Compute hashes of all square submatrices of size `k` in matrix **B**.
4. If any hash matches, a common square of size `k` exists.
5. Increase or decrease the binary search range accordingly.

---

## Algorithm

1. Read both matrices.
2. Precompute powers required for rolling hash.
3. Perform Binary Search on square size.
4. For each candidate size:
   - Generate all hashes from matrix A.
   - Generate all hashes from matrix B.
   - Check whether any hash is common.
5. Print the largest valid square size.

---
