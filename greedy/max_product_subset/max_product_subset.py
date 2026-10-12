class Solution:
    def findMaxProduct(self, arr):
        MOD = 10**9 + 7

        negatives = []
        product = 1
        zeros = 0

        for num in arr:
            if num == 0:
                zeros += 1
            else:
                product *= num
                if num < 0:
                    negatives.append(num)

        if len(arr) == 1:
            return arr[0]

        if len(negatives) == 1 and zeros == len(arr) - 1:
            return 0

        if len(negatives) % 2 == 1:
            product //= max(negatives)

        if product == 1 and zeros == len(arr):
            return 0

        return product % MOD
