# Max Equal Sum in 3 Stacks

## Problem
Given three stacks represented by arrays, where the first element is the top of each stack, find the maximum possible equal sum after removing zero or more elements from the tops.

Return `0` if an equal sum is not possible.

## Approach – Greedy
- Calculate the initial sum of all three stacks.
- Use three pointers to track the top elements.
- Compare the three current sums.
- Remove the top element from the stack with the largest sum.
- Update that stack's sum.
- Repeat until all three sums become equal or one stack becomes empty.
- Return the equal sum if found; otherwise, return `0`.

## Example

**Input:**
```text
s1 = [3, 2, 1, 1, 1]
s2 = [4, 3, 2]
s3 = [2, 5, 4, 1]
```

**Output:** `5`


