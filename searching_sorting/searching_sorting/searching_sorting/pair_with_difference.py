from typing import List

class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        arr.sort()

        i, j = 0, 1
        n = len(arr)

        while j < n:
            diff = arr[j] - arr[i]

            if i != j and diff == x:
                return True
            elif diff < x:
                j += 1
            else:
                i += 1
                if i == j:
                    j += 1

        return False
