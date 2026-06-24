# Common Elements in All Rows of a Matrix

## Problem Statement

Given a matrix, find all elements that are present in every row.

Return all common elements.

## Example

Input:

```text
[
 [1, 2, 1, 4, 8],
 [3, 7, 8, 5, 1],
 [8, 7, 7, 3, 1],
 [8, 1, 2, 7, 9]
]
```

Output:

```text
[1, 8]
```

Explanation:

Both 1 and 8 are present in all rows.

## Approach

I start by storing all elements of the first row in a set.

Then I compare it with every other row using set intersection.

After processing all rows, only the elements that appear in every row remain in the set.

Finally, I return those elements.
