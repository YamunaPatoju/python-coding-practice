class Solution:
    def addTwoLists(self, head1, head2):
        def reverse(head):
            prev = None
            curr = head

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            return prev

        head1 = reverse(head1)
        head2 = reverse(head2)

        carry = 0
        dummy = Node(0)
        curr = dummy

        while head1 or head2 or carry:
            total = carry

            if head1:
                total += head1.data
                head1 = head1.next

            if head2:
                total += head2.data
                head2 = head2.next

            curr.next = Node(total % 10)
            curr = curr.next
            carry = total // 10

        result = reverse(dummy.next)

        while result and result.data == 0 and result.next:
            result = result.next

        return result
