class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = list(zip(deadline, profit))
        jobs.sort(key=lambda x: x[1], reverse=True)

        n = len(jobs)
        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        count = 0
        total_profit = 0

        for d, p in jobs:
            slot = find(min(d, n))

            if slot > 0:
                count += 1
                total_profit += p

                # Mark this slot as occupied
                parent[slot] = find(slot - 1)

        return [count, total_profit]
