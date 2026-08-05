'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def reverseKGroup(self, head, k):
        if not head:
            return head

        curr = head
        prev = None
        nxt = None
        count = 0

  
        while curr and count < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1

        if curr:
            head.next = self.reverseKGroup(curr, k)

        return prev
