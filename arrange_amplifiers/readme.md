# ARRANGE — Arranging Amplifiers

## Problem
Given a set of positive integers representing amplifier factors, arrange them to produce the strongest signal. If multiple arrangements produce the same strength, output the lexicographically largest arrangement, placing larger amplifiers first when possible.

## Approach
Use sorting and handle the value `1` separately.

- Amplifiers with value `1` do not increase the signal strength.
- Place all `1`s at the beginning.
- Place the remaining amplifiers in descending order to maximize the exponentiation chain.

## Algorithm
1. Read the number of test cases.
2. For each test case, read `n` and the amplifier values.
3. Sort the values in ascending order.
4. Count the number of `1`s.
5. Keep all `1`s at the beginning.
6. Append the remaining values in descending order.
7. Print the resulting arrangement.

## Example

**Input:**
```text
2
3
5 6 4
2
2 3
```

**Output:**
```text
6 5 4
2 3
```


