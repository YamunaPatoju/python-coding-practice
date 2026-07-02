# Count the Reversals

## Problem Statement

Given a string consisting only of opening `{` and closing `}` braces, find the minimum number of reversals required to make the expression balanced.

If the length of the string is odd, return `-1` since it cannot be balanced.

## Example 1

**Input:**

```text
s = "}{{}}{{{"
```

**Output:**

```text
3
```

## Example 2

**Input:**

```text
s = "{{}{{{}{{}}{{"
```

**Output:**

```text
-1
```

## Approach

- If the string length is odd, return `-1`.
- Use a stack to remove all balanced brace pairs.
- Count the remaining unmatched opening and closing braces.
- The minimum reversals required are:

```text
(open + 1) // 2 + (close + 1) // 2
```

where:
- `open` = unmatched `{`
- `close` = unmatched `}`

