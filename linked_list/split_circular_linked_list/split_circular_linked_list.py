class Solution:
    def splitList(self, head):
        if not head or head.next == head:
            return [head, None]

        slow = head
        fast = head

        while fast.next != head and fast.next.next != head:
            slow = slow.next
            fast = fast.next.next

        if fast.next.next == head:
            fast = fast.next

        head1 = head
        head2 = slow.next

        slow.next = head1
        fast.next = head2

        return [head1, head2]
