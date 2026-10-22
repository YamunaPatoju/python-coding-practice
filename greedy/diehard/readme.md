# DIEHARD — Die Hard

## Problem
Given initial health `H` and armor `A`, determine the maximum time a character can survive by moving between air, water, and fire.

The character must change environments after every unit of time. If health or armor becomes less than or equal to zero, the character dies.

## Environment Effects
- **Air:** Health +3, Armor +2
- **Water:** Health -5, Armor -10
- **Fire:** Health -20, Armor +5

## Approach
Use recursion to explore every valid sequence of environment changes. Each move must go to a different environment from the current one.

For each environment:
1. Apply its health and armor changes.
2. Stop if health or armor becomes zero or negative.
3. Otherwise, add one unit of survival time and explore the other two environments.
4. Return the maximum survival time among all possible starting environments.

## Algorithm
1. Start separately in air, water, and fire.
2. Apply the selected environment's effects.
3. If health or armor becomes non-positive, return `0`.
4. Recursively explore both permitted next environments.
5. Return `1` plus the larger result.
6. Print the maximum result across all three starting choices.

## Example

**Input:**
```text
3
2 10
4 4
20 8
```

**Output:**
```text
1
1
5
```

