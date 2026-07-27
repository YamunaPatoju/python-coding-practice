# Bishu and Soldiers

## Problem Statement

Bishu has to fight `N` soldiers, each having a certain power.

For every round:

- Bishu is given a power `M`.
- He can defeat all soldiers whose power is **less than or equal to M**.
- After every round, all defeated soldiers come back to life.

For each query, print:

1. Number of soldiers Bishu can defeat.
2. Sum of the powers of those soldiers.

---

## Example

### Input

```text
7
1 2 3 4 5 6 7
3
3
10
2
```

### Output

```text
3 6
7 28
2 3
```

---

## Approach

Since there are many queries, checking every soldier for every query would be slow.

Instead:

1. Sort the soldiers' powers.
2. Build a Prefix Sum array.
3. For every query:
   - Use Binary Search (`bisect_right`) to find how many soldiers have power `≤ M`.
   - Use the Prefix Sum array to calculate the total power instantly.

---

## Algorithm

1. Read the powers of all soldiers.
2. Sort the array.
3. Build a Prefix Sum array.
4. For each query:
   - Find the first index greater than `M` using Binary Search.
   - That index is the number of soldiers Bishu can defeat.
   - Use the Prefix Sum array to obtain the total power.
5. Print the count and total power.

---

