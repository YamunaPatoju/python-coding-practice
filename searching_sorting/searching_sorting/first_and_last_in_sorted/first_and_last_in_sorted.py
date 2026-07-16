class Solution:
    def find(self, arr, x):

        def first():
            low, high = 0, len(arr) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] == x:
                    ans = mid
                    high = mid - 1
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1

            return ans

        def last():
            low, high = 0, len(arr) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] == x:
                    ans = mid
                    low = mid + 1
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1

            return ans

        return [first(), last()]
