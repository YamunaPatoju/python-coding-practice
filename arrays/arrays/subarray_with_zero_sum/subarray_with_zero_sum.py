def subArrayExists(self, arr):
        prefix_sum = 0
        seen = set()

        for num in arr:
            prefix_sum += num

            if prefix_sum == 0 or prefix_sum in seen:
                return True

            seen.add(prefix_sum)

        return False
