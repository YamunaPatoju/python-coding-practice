def inversionCount(self, arr):
        self.count = 0

        def merge_sort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            merge(left, mid, right)

        def merge(left, mid, right):
            temp = []
            i = left
            j = mid + 1

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    self.count += (mid - i + 1)
                    j += 1

            while i <= mid:
                temp.append(arr[i])
                i += 1

            while j <= right:
                temp.append(arr[j])
                j += 1

            for k in range(len(temp)):
                arr[left + k] = temp[k]

        merge_sort(0, len(arr) - 1)
        return self.count
