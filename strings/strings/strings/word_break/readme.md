# Word Break

## Problem Statement

Given a string `s` and a dictionary of words, determine whether the string can be formed by concatenating one or more words from the dictionary.

A dictionary word can be used any number of times.

## Example 1

**Input:**

```text
s = "ilike"
dictionary = ["i", "like", "gfg"]
```

**Output:**

```text
true
```

## Example 2

**Input:**

```text
s = "ilikegfg"
dictionary = ["i", "like", "man", "india", "gfg"]
```

**Output:**

```text
true
```

## Example 3

**Input:**

```text
s = "ilikemangoes"
dictionary = ["i", "like", "man", "india", "gfg"]
```

**Output:**

```text
false
```

## Approach

- Store all dictionary words in a set for fast lookup.
- Use Dynamic Programming.
- Let `dp[i]` indicate whether the first `i` characters can be formed.
- For each position, check all previous partitions.
- If a valid partition exists and the substring is in the dictionary, mark `dp[i]` as `True`.
