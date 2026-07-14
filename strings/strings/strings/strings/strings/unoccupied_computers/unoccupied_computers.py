class Solution:
    def solve(self, n, s):

        inside = set()
        rejected = set()
        free = n
        ans = 0

        for ch in s:

            if ch not in inside and ch not in rejected:

                if free > 0:
                    inside.add(ch)
                    free -= 1
                else:
                    rejected.add(ch)
                    ans += 1

            elif ch in inside:
                inside.remove(ch)
                free += 1

            else:
                rejected.remove(ch)

        return ans
