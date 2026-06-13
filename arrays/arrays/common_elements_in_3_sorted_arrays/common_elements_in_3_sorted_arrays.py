def commonElements(self, a, b, c):
        i = j = k = 0
        result = []

        while i < len(a) and j < len(b) and k < len(c):

            if a[i] == b[j] == c[k]:
                if not result or result[-1] != a[i]:
                    result.append(a[i])

                i += 1
                j += 1
                k += 1

            elif a[i] < b[j]:
                i += 1

            elif b[j] < c[k]:
                j += 1

            else:
                k += 1

        return result
