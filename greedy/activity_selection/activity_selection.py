class Solution:
    def activitySelection(self, start, finish):
        activities = list(zip(start, finish))

        activities.sort(key=lambda x: x[1])

        count = 0
        last_finish = -1

        for start_time, finish_time in activities:
            if start_time > last_finish:
                count += 1
                last_finish = finish_time

        return count
