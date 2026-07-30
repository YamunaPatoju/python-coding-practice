# Weighted Job Scheduling

## Problem Statement

You are given `n` jobs, where each job has:

- Start Time
- End Time
- Profit

The goal is to schedule a subset of non-overlapping jobs such that the **total profit is maximized**.

Two jobs overlap if the start time of one job is earlier than the finish time of another.

---

## Example 1

### Input

```text
[
 [1,2,50],
 [3,5,20],
 [6,19,100],
 [2,100,200]
]
```

### Output

```text
250
```

### Explanation

Choose:

```text
(1,2,50)
(2,100,200)
```

Total Profit:

```text
50 + 200 = 250
```

---

## Example 2

### Input

```text
[
 [1,3,60],
 [2,5,50],
 [4,6,70],
 [5,7,30]
]
```

### Output

```text
130
```

---

## Approach

The solution combines:

- Sorting
- Binary Search
- Dynamic Programming (Memoization)

### Step 1

Sort jobs by **start time**.

---

### Step 2

For every job, use **Binary Search** to find the next job that starts after the current job finishes.

---

### Step 3

For every job there are two choices:

- Take the current job and add the best profit from the next compatible job.
- Skip the current job.

Store the answer using memoization.

---

## Algorithm

1. Sort all jobs by start time.
2. For each job:
   - Find the next compatible job using Binary Search.
   - Compute:
     - Take current job.
     - Skip current job.
3. Store the maximum profit in the DP array.
4. Return the answer from the first job.

---

