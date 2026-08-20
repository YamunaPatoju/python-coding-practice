import heapq

class Solution:
    def flatten(self, head):
        if head is None:
            return None

        heap = []
        curr = head

        while curr:
            heapq.heappush(heap, (curr.data, id(curr), curr))
            curr = curr.next

        dummy = Node(0)
        temp = dummy

        while heap:
            _, _, node = heapq.heappop(heap)

            temp.bottom = node
            temp = node

            if node.bottom:
                heapq.heappush(heap, (node.bottom.data, id(node.bottom), node.bottom))

        temp.bottom = None
        return dummy.bottom
