class Solution:
    def maxStop(self, n, trains):
        platforms = {}

        for arrival, departure, platform in trains:
            if platform not in platforms:
                platforms[platform] = []
            platforms[platform].append((arrival, departure))

        count = 0

        for platform in platforms:
            platforms[platform].sort(key=lambda x: x[1])

            last_departure = -1

            for arrival, departure in platforms[platform]:
                if arrival >= last_departure:
                    count += 1
                    last_departure = departure

        return count
