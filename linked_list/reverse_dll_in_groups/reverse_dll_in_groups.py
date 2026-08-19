class Solution:
    def reverseDLL(self, head, k):
        if head is None or k <= 1:
            return head

        curr = head
        prev = None
        count = 0

        while curr and count < k:
            next_node = curr.next
            curr.next = prev
            curr.prev = next_node
            prev = curr
            curr = next_node
            count += 1

        head.next = curr

        if curr:
            curr.prev = head

        return prev
