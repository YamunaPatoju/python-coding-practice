class Solution:
    def minSwaps(self, s):

        imbalance = 0
        open_brackets = 0
        swaps = 0

        for ch in s:

            if ch == '[':
                open_brackets += 1

                if imbalance > 0:
                    swaps += imbalance
                    imbalance -= 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    imbalance += 1

        return swaps
