# Waiting and Turnaround Time in Shortest Job First

## Problem
Given the arrival times and burst times of processes, schedule them using non-preemptive Shortest Job First (SJF) and return the average waiting time and average turnaround time.

## Approach
- Sort processes by arrival time.
- Use a min-heap to select the arrived process with the shortest burst time.
- If no process is available, advance time to the next arrival.
- Calculate waiting time and turnaround time for every process.
- Round both averages to two decimal places using half-up rounding.

## Algorithm
1. Store each process as `(arrival_time, burst_time, process_id)`.
2. Sort processes by arrival time.
3. Add all processes that have arrived to a min-heap ordered by burst time.
4. Execute the process with the shortest burst time until completion.
5. Calculate turnaround time as `completion_time - arrival_time`.
6. Calculate waiting time as `turnaround_time - burst_time`.
7. Repeat until all processes are completed.
8. Calculate and return the average waiting time and average turnaround time.

## Example
**Input:** `arrivalTime = [0, 0, 0]`, `burstTime = [4, 2, 3]`

**Execution order:** Process 2 → Process 3 → Process 1

**Waiting times:** `[5, 0, 2]`

**Turnaround times:** `[9, 2, 5]`

**Output:** `[2.33, 5.33]`

