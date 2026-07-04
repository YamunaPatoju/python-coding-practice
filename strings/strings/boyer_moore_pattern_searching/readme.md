# Boyer Moore Pattern Searching (Bad Character Heuristic)

## Problem Statement

Given a text string and a pattern string, find all occurrences of the pattern inside the text using the **Boyer-Moore Algorithm**.

Unlike the Naive or KMP algorithms, Boyer-Moore starts comparing characters from the **end of the pattern**, allowing it to skip many unnecessary comparisons.

---

## Example 1

**Input**

```text
Text    = "THIS IS A TEST TEXT"
Pattern = "TEST"
```

**Output**

```text
[10]
```

---

## Example 2

**Input**

```text
Text    = "AABAACAADAABAABA"
Pattern = "AABA"
```

**Output**

```text
[0, 9, 12]
```

---

# Bad Character Heuristic

The algorithm preprocesses the pattern and stores the **last occurrence** of every character.

Whenever a mismatch occurs:

- If the mismatched character exists in the pattern, align its last occurrence.
- Otherwise, skip the entire mismatched character.

This allows the pattern to jump multiple positions instead of shifting by one.

---

## Algorithm

1. Build the Bad Character table.
2. Start comparing from the last character of the pattern.
3. If characters match, continue moving left.
4. If mismatch occurs:
   - Find the last occurrence of the mismatched character.
   - Shift the pattern accordingly.
5. If the entire pattern matches, record the index.
6. Continue searching.
