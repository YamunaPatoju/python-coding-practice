import heapq

class Solution:
    def mergeKLists(self, arr):
        heap = []

        for node in arr:
            if node:
                heapq.heappush(heap, (node.data, id(node), node))

        dummy = Node(0)
        curr = dummy

        while heap:
            _, _, node = heapq.heappop(heap)

            curr.next = node
            curr = node

            if node.next:
                heapq.heappush(heap, (node.next.data, id(node.next), node.next))

        curr.next = None

        return dummy.next
