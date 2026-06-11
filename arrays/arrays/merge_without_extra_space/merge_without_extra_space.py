def mergeArrays(self, a, b):
        i = len(a) - 1
        j = 0

        while i >= 0 and j < len(b):

            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
                i -= 1
                j += 1
            else:
                break

        a.sort()
        b.sort()
