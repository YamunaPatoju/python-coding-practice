class Solution:
    def generateIp(self, s):

        result = []

        def valid(part):
            if len(part) > 1 and part[0] == '0':
                return False
            return 0 <= int(part) <= 255

        def backtrack(index, parts):

            if len(parts) == 4:
                if index == len(s):
                    result.append(".".join(parts))
                return

            for length in range(1, 4):

                if index + length > len(s):
                    break

                part = s[index:index + length]

                if valid(part):
                    backtrack(index + length, parts + [part])

        backtrack(0, [])

        return result
