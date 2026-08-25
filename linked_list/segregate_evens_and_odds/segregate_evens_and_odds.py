class Solution:
    def divide(self, head):
        if head is None:
            return None

        even_head = even_tail = None
        odd_head = odd_tail = None

        curr = head

        while curr:
            next_node = curr.next
            curr.next = None

            if curr.data % 2 == 0:
                if even_head is None:
                    even_head = even_tail = curr
                else:
                    even_tail.next = curr
                    even_tail = curr
            else:
                if odd_head is None:
                    odd_head = odd_tail = curr
                else:
                    odd_tail.next = curr
                    odd_tail = curr

            curr = next_node

        if even_head is None:
            return odd_head

        even_tail.next = odd_head

        return even_head
