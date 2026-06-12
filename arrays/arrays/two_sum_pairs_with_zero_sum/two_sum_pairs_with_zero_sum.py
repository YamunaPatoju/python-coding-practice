def getPairs(self, arr):
        result = []

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == 0:
                    pair = sorted([arr[i], arr[j]])

                    if pair not in result:
                        result.append(pair)

        result.sort()
        return result
