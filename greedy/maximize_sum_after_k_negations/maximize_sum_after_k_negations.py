class Solution:
    def maximizeSum(self, arr, k):
        arr.sort()

        for i in range(len(arr)):
            if k > 0 and arr[i] < 0:
                arr[i] = -arr[i]
                k -= 1
            else:
                break

        if k % 2 == 1:
            arr.sort()
            arr[0] = -arr[0]

        return sum(arr)
