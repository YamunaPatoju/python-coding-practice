class IntervalNode:
    def __init__(self, interval):
        self.interval = interval
        self.max = interval[1]
        self.left = None
        self.right = None


class Solution:
    def doOverlap(self, i1, i2):
        return i1[0] < i2[1] and i2[0] < i1[1]

    def insert(self, root, interval):
        if root is None:
            return IntervalNode(interval)

        if interval[0] < root.interval[0]:
            root.left = self.insert(root.left, interval)
        else:
            root.right = self.insert(root.right, interval)

        root.max = max(root.max, interval[1])

        return root

    def overlapSearch(self, root, interval):
        if root is None:
            return None

        if self.doOverlap(root.interval, interval):
            return root.interval

        if root.left is not None and root.left.max > interval[0]:
            return self.overlapSearch(root.left, interval)

        return self.overlapSearch(root.right, interval)

    def printConflicting(self, appointments):
        if not appointments:
            return

        root = None

        root = self.insert(root, appointments[0])

        for i in range(1, len(appointments)):
            conflict = self.overlapSearch(root, appointments[i])

            if conflict is not None:
                print(
                    f"[{appointments[i][0]},{appointments[i][1]}] "
                    f"Conflicts with "
                    f"[{conflict[0]},{conflict[1]}]"
                )

            root = self.insert(root, appointments[i])
