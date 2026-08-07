class Solution:
    def removeDuplicates(self, head):
        seen = set()
        curr = head
        prev = None

        while curr:
            if curr.data in seen:
                prev.next = curr.next
            else:
                seen.add(curr.data)
                prev = curr

            curr = curr.next

        return head
