class Solution:
    def minSwap(self, arr, k):

        good = 0

        for num in arr:
            if num <= k:
                good += 1

        bad = 0

        for i in range(good):
            if arr[i] > k:
                bad += 1

        ans = bad

        left = 0
        right = good

        while right < len(arr):

            if arr[left] > k:
                bad -= 1

            if arr[right] > k:
                bad += 1

            ans = min(ans, bad)

            left += 1
            right += 1

        return ans
