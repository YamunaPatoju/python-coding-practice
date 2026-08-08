class Solution:
    def addOne(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head = prev
        curr = head
        carry = 1

        while curr and carry:
            total = curr.data + carry
            curr.data = total % 10
            carry = total // 10

            if carry and curr.next is None:
                curr.next = Node(0)

            curr = curr.next

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        if carry:
            new_node = Node(carry)
            new_node.next = prev
            prev = new_node

        return prev
