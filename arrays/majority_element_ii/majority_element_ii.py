class Solution:
    def majorityElement(self, nums):
        result = []

        for num in set(nums):
            if nums.count(num) > len(nums) // 3:
                result.append(num)

        return result
