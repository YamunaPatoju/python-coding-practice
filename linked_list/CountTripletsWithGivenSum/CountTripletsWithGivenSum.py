class Solution:
    def countTriplets(self, head, x):
        count = 0
        first = head

        while first:
            second = first.next
            last = self.getLast(head)

            while second and last and second != last and second.prev != last:
                total = first.data + second.data + last.data

                if total == x:
                    count += 1
                    second = second.next
                    last = last.prev
                elif total < x:
                    second = second.next
                else:
                    last = last.prev

            first = first.next

        return count

    def getLast(self, head):
        last = head

        while last and last.next:
            last = last.next

        return last
