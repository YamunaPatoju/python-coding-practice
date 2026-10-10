class Solution:
    def minimumDays(self, S, N, M):
        if S >= 7 and N * 6 < M * 7:
            return -1

        if N < M:
            return -1

        total_food = S * M
        return (total_food + N - 1) // N
