class Solution:
    def selectKcities(self, k, mat):
        n = len(mat)
        answer = float('inf')

        for mask in range(1, 1 << n):
            if mask.bit_count() != k:
                continue

            max_dist = 0

            for city in range(n):
                nearest = float('inf')

                for server in range(n):
                    if mask & (1 << server):
                        nearest = min(nearest, mat[city][server])

                max_dist = max(max_dist, nearest)

            answer = min(answer, max_dist)

        return answer
