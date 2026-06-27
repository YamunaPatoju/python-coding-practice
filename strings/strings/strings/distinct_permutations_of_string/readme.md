# Distinct Permutations of a String

## Problem Statement

Given a string `s` that may contain duplicate characters, generate and return all unique permutations of the string.

## Example 1

**Input:**

```text
s = "ABC"
```

**Output:**

```text
["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
```

## Example 2

**Input:**

```text
s = "ABSG"
```

**Output:**

```text
["ABGS", "ABSG", "AGBS", "AGSB", "ASBG", "ASGB", "BAGS", "BASG", "BGAS", "BGSA", "BSAG", "BSGA", "GABS", "GASB", "GBAS", "GBSA", "GSAB", "GSBA", "SABG", "SAGB", "SBAG", "SBGA", "SGAB", "SGBA"]
```

## Example 3

**Input:**

```text
s = "AAA"
```

**Output:**

```text
["AAA"]
```

## Approach

- Sort the characters of the string.
- Use backtracking to generate all permutations.
- Use a `used` array to track selected characters.
- Skip duplicate characters to avoid repeated permutations.
- Store each completed permutation in the result list.

        return result
```
