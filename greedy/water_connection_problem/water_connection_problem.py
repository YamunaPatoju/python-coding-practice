class Solution:
    def solve(self, n, p, a, b, d):
        outgoing = {}
        incoming = set()

        for i in range(p):
            outgoing[a[i]] = (b[i], d[i])
            incoming.add(b[i])

        result = []

        for house in range(1, n + 1):
            if house in outgoing and house not in incoming:
                current = house
                minimum_diameter = float("inf")

                while current in outgoing:
                    next_house, diameter = outgoing[current]
                    minimum_diameter = min(minimum_diameter, diameter)
                    current = next_house

                result.append([house, current, minimum_diameter])

        return result
