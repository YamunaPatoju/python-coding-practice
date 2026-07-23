class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        n = len(arr)
        count = 0

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total < sum:
                    count += (right - left)
                    left += 1
                else:
                    right -= 1

        return count
