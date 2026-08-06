'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def removeLoop(self, head):
        if not head or not head.next:
            return

        slow = head
        fast = head

        # Detect loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return

        # Loop starts at head
        if slow == head:
            while fast.next != head:
                fast = fast.next
            fast.next = None
            return

        # Find start of loop
        slow = head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

        # Remove loop
        fast.next = None
