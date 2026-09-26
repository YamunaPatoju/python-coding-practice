# Sum Pairs Across Two BSTs

## Problem

Given the roots of two Binary Search Trees (BSTs), `root1` and `root2`, and an integer `x`, find the number of pairs `(a, b)` such that:

* `a` belongs to the first BST.
* `b` belongs to the second BST.
* `a + b = x`.

## Approach

We use a **set** to store all values from the first BST.

Then, while traversing the second BST, for every value `b` we check whether:

```text
x - b
```

exists in the set.

If it exists, then:

```text
a + b = x
```

and we found a valid pair.

## Algorithm

```text
1. Traverse the first BST.
2. Store every node value in a set.
3. Traverse the second BST.
4. For each node value b:
      required = x - b
5. If required exists in the set, increment count.
6. Return count.
```

## Example

### Input

```text
root1 = [2, 1, 3]
root2 = [5, 4, 6]
x = 6
```

Values in the first BST:

```text
1, 2, 3
```

Check values from the second BST:

```text
5 → 6 - 5 = 1  ✓
4 → 6 - 4 = 2  ✓
6 → 6 - 6 = 0  ✗
```

Valid pairs:

```text
(1, 5)
(2, 4)
```

### Output

```text
2
```

