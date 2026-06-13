def rearrange(self, arr):
        pos = []
        neg = []

        for num in arr:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)

        result = []
        i = j = 0

        while i < len(pos) and j < len(neg):
            result.append(pos[i])
            result.append(neg[j])
            i += 1
            j += 1

        while i < len(pos):
            result.append(pos[i])
            i += 1

        while j < len(neg):
            result.append(neg[j])
            j += 1

        for i in range(len(arr)):
            arr[i] = result[i]

        return arr
