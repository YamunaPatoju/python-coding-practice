class Solution:
    def longestConsecutive(self, arr):
        nums = set(arr)
        longest = 0

        for num in nums:

            if num - 1 not in nums:

                current = num
                count = 1

                while current + 1 in nums:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest
