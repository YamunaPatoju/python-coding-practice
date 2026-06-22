class Solution:
    def rowWithMax1s(self, arr):
        max_ones = 0
        row_index = -1

        for i in range(len(arr)):
            count = arr[i].count(1)

            if count > max_ones:
                max_ones = count
                row_index = i

        return row_index
