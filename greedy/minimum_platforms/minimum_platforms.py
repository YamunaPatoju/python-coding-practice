class Solution:
    def minPlatform(self, arr, dep):
        arr.sort()
        dep.sort()

        i = 0
        j = 0
        platforms = 0
        answer = 0
        n = len(arr)

        while i < n and j < n:
            if arr[i] <= dep[j]:
                platforms += 1
                answer = max(answer, platforms)
                i += 1
            else:
                platforms -= 1
                j += 1

        return answer
