# Parenthesis Checker

## Problem Statement

Given a string containing the characters `(`, `)`, `{`, `}`, `[` and `]`, determine whether the expression is balanced.

An expression is balanced if every opening bracket has a matching closing bracket in the correct order.

## Example 1

**Input:**

```text
[{()}]
```

**Output:**

```text
true
```

## Example 2

**Input:**

```text
[()()]{}
```

**Output:**

```text
true
```

## Example 3

**Input:**

```text
([]
```

**Output:**

```text
false
```

## Approach

- Use a stack.
- Push every opening bracket onto the stack.
- For every closing bracket, check if it matches the top of the stack.
- If it doesn't match or the stack is empty, return `false`.
- At the end, the stack should be empty for the expression to be balanced.

