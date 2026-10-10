# Check for Survival on Island

## Problem

A person must survive on an island for `S` days.

- `N` is the maximum amount of food that can be bought per day.
- `M` is the amount of food required per day.
- The shop is open every day except Sunday.
- Initially, there is no food, and the first day is Monday.

Find the minimum number of days on which food must be purchased. Return `-1` if survival is impossible.

## Approach

Use a **Greedy** approach.

1. If `N < M`, survival is impossible because the person cannot buy enough food for one day.
2. If the survival period includes Sundays, check whether the food available during the six shopping days each week can meet the weekly requirement.
3. Calculate the total food required for `S` days.
4. Divide the total food by `N`, rounding up to get the minimum number of purchase days.

## Algorithm

1. If `S >= 7` and `6 × N < 7 × M`, return `-1`.
2. If `N < M`, return `-1`.
3. Calculate `total_food = S × M`.
4. Calculate the minimum purchase days using ceiling division:

   `(total_food + N - 1) // N`

5. Return the result.

## Example 1

### Input

```text
S = 10
N = 16
M = 2
```

### Output

```text
2
```


