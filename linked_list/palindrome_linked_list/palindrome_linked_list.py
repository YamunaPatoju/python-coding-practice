class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        left = head
        right = prev

        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next

        return True
