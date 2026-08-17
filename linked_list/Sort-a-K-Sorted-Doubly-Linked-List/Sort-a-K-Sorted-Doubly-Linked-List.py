import heapq

def sortedDll(head, k):
    if head is None:
        return None

    heap = []
    curr = head
    count = 0

    for _ in range(k + 1):
        if curr is None:
            break
        heapq.heappush(heap, (curr.data, count, curr))
        count += 1
        curr = curr.next

    new_head = None
    tail = None

    while heap:
        _, _, node = heapq.heappop(heap)

        if new_head is None:
            new_head = node
            tail = node
        else:
            tail.next = node
            node.prev = tail
            tail = node

        if curr:
            heapq.heappush(heap, (curr.data, count, curr))
            count += 1
            curr = curr.next

    tail.next = None
    new_head.prev = None

    return new_head
