class Solution:
    def getMinMax(self, arr):

        mn = arr[0]
        mx = arr[0]

        for num in arr:

            if num < mn:
                mn = num

            if num > mx:
                mx = num

        return [mn, mx]
