class Solution:
    def isCircular(self, head):
        if head is None:
            return True

        curr = head.next

        while curr is not None and curr != head:
            curr = curr.next

        return curr == head
