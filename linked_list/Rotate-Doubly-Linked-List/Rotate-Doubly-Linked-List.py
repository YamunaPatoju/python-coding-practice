class Solution:
    def rotateDLL(self, head, k):
        if head is None or head.next is None:
            return head

        tail = head
        n = 1

        while tail.next:
            tail = tail.next
            n += 1

        k %= n

        if k == 0:
            return head

        tail.next = head
        head.prev = tail

        new_head = head

        for _ in range(k):
            new_head = new_head.next

        new_tail = new_head.prev

        new_tail.next = None
        new_head.prev = None

        return new_head
