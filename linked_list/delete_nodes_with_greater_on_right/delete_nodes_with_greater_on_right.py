class Solution:
    def compute(self, head):
        if head is None:
            return None

        prev = None
        curr = head

        while curr:
            curr.prev = prev
            prev = curr
            curr = curr.next

        curr = prev
        max_val = curr.data
        new_head = curr

        curr = curr.prev

        while curr:
            prev = curr.prev

            if curr.data >= max_val:
                curr.next = new_head
                new_head = curr
                max_val = curr.data

            curr = prev

        return new_head
