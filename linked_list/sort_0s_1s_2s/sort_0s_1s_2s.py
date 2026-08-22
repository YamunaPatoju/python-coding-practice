class Solution:
    def segregate(self, head):
        count = [0, 0, 0]

        curr = head

        while curr:
            count[curr.data] += 1
            curr = curr.next

        curr = head

        for i in range(3):
            while count[i] > 0:
                curr.data = i
                curr = curr.next
                count[i] -= 1

        return head
