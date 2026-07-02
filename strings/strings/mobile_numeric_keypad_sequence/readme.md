# Convert a Sentence into its Equivalent Mobile Numeric Keypad Sequence

## Problem Statement

Given a sentence containing uppercase English letters and spaces, convert it into its equivalent mobile numeric keypad sequence.

A space is represented by `0`.

## Example 1

**Input:**

```text
S = "GFG"
```

**Output:**

```text
43334
```

## Example 2

**Input:**

```text
S = "HEY U"
```

**Output:**

```text
4433999088
```

## Approach

- Create a mapping of each uppercase letter to its corresponding mobile keypad sequence.
- Map spaces to `0`.
- Traverse the string and append the mapped sequence for each character.
- Return the final sequence.
