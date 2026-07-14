class Solution:
    def match(self, wild, pattern):

        i = 0
        j = 0
        star = -1
        match = 0

        while j < len(pattern):

            if i < len(wild) and (wild[i] == pattern[j] or wild[i] == '?'):
                i += 1
                j += 1

            elif i < len(wild) and wild[i] == '*':
                star = i
                match = j
                i += 1

            elif star != -1:
                i = star + 1
                match += 1
                j = match

            else:
                return False

        while i < len(wild) and wild[i] == '*':
            i += 1

        return i == len(wild)
