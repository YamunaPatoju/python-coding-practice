class Solution:
    def minSubset(self, arr):
        arr.sort(reverse=True)

        total = sum(arr)
        selected_sum = 0

        for i in range(len(arr)):
            selected_sum += arr[i]
            total -= arr[i]

            if selected_sum > total:
                return i + 1

        return len(arr)
