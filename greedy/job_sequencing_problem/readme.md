# Job Sequencing Problem

## Problem

Given `deadline[]` and `profit[]` for jobs, schedule jobs so that:

* Each job takes one unit of time.
* A job must be completed on or before its deadline.
* Only one job can be done in each time slot.
* The goal is to maximize total profit.

Return:

* Maximum number of jobs completed.
* Maximum total profit.

## Approach

1. Combine `deadline` and `profit` into jobs.
2. Sort jobs by profit in descending order.
3. Use **Disjoint Set Union (DSU)** to quickly find the latest available time slot.
4. If a valid slot is available, schedule the job.
5. Merge the occupied slot with the previous available slot.

## Algorithm

* Sort all jobs by decreasing profit.
* Create a DSU array where each index represents a time slot.
* For each job:

  * Find the latest available slot up to its deadline.
  * If the slot is greater than `0`, schedule the job.
  * Add its profit.
  * Mark the slot as occupied by connecting it to the previous slot.
* Return the job count and total profit.

## Example

### Input

```text
deadline = [5, 4, 1, 3, 4]
profit   = [14, 7, 5, 10, 6]
```

### Output

```text
[5, 42]
```


