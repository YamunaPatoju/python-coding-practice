class Solution:
    def maxMeetings(self, s, f):
        meetings = []

        for i in range(len(s)):
            meetings.append((f[i], i + 1, s[i]))

        meetings.sort()

        result = []
        last_finish = -1

        for finish, index, start in meetings:
            if start > last_finish:
                result.append(index)
                last_finish = finish

        return sorted(result)
