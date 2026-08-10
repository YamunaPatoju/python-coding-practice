class Solution:
    def findIntersection(self, head1, head2):
        dummy = Node(0)
        curr = dummy

        while head1 and head2:
            if head1.data == head2.data:
                curr.next = Node(head1.data)
                curr = curr.next
                head1 = head1.next
                head2 = head2.next
            elif head1.data < head2.data:
                head1 = head1.next
            else:
                head2 = head2.next

        return dummy.next
