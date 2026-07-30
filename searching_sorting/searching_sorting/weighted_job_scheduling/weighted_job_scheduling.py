def findNextJob(i, jobs):
    end = jobs[i][1]
    ans = len(jobs)

    left = i + 1
    right = len(jobs) - 1

    while left <= right:
        mid = (left + right) // 2

        if jobs[mid][0] >= end:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


def maxProfitRecur(i, jobs, dp):
    if i == len(jobs):
        return 0

    if dp[i] != -1:
        return dp[i]

    nextJob = findNextJob(i, jobs)

    take = jobs[i][2] + maxProfitRecur(nextJob, jobs, dp)
    skip = maxProfitRecur(i + 1, jobs, dp)

    dp[i] = max(take, skip)
    return dp[i]


def maxProfit(jobs):
    jobs.sort()

    dp = [-1] * len(jobs)

    return maxProfitRecur(0, jobs, dp)


# Driver Code
jobs = [
    [1, 2, 50],
    [3, 5, 20],
    [6, 19, 100],
    [2, 100, 200]
]

print(maxProfit(jobs))
