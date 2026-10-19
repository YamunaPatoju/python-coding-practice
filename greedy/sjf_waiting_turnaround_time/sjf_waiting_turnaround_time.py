import heapq
from decimal import Decimal, ROUND_HALF_UP

class Solution:
    def averageTimes(self, arrivalTime, burstTime):
        n = len(arrivalTime)

        processes = sorted(
            (arrivalTime[i], burstTime[i], i)
            for i in range(n)
        )

        heap = []
        time = 0
        index = 0
        total_waiting = 0
        total_turnaround = 0

        while index < n or heap:
            if not heap and time < processes[index][0]:
                time = processes[index][0]

            while index < n and processes[index][0] <= time:
                arrival, burst, pid = processes[index]
                heapq.heappush(heap, (burst, arrival, pid))
                index += 1

            burst, arrival, pid = heapq.heappop(heap)
            time += burst

            turnaround = time - arrival
            waiting = turnaround - burst

            total_waiting += waiting
            total_turnaround += turnaround

        avg_waiting = (
            Decimal(total_waiting) / Decimal(n)
        ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        avg_turnaround = (
            Decimal(total_turnaround) / Decimal(n)
        ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        return [float(avg_waiting), float(avg_turnaround)]
