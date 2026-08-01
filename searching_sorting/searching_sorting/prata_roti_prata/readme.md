# PRATA - Roti Prata

## Problem Statement

Given `P` pratas to cook and `L` cooks with different ranks.

A cook with rank `R` cooks:

- 1st prata in `R` minutes
- 2nd prata in `2R` minutes
- 3rd prata in `3R` minutes
- ...

Find the **minimum time** required to cook all `P` pratas.

---

## Example

### Input

```text
P = 10

Ranks = [1,2,3,4]
```

### Output

```text
12
```

---

## Approach

The answer is searched using **Binary Search**.

### Observation

If all cooks can prepare at least `P` pratas in `T` minutes, then any time greater than `T` is also valid.

This monotonic property allows Binary Search.

---

## Algorithm

1. Set:
   - Low = 0
   - High = maximum possible cooking time.
2. Binary Search on time.
3. For every candidate time:
   - Compute how many pratas every cook can prepare.
4. If total pratas ≥ P:
   - Search left.
5. Otherwise:
   - Search right.
6. Return minimum valid time.

---

