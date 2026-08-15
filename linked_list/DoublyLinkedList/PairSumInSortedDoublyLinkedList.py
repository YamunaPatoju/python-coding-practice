class Solution:
    def givenSumPairs(self, head, target):
        ans = []
        left = head
        right = head

        while right.next:
            right = right.next

        while left != right and left.prev != right:
            total = left.data + right.data

            if total == target:
                ans.append([left.data, right.data])
                left = left.next
                right = right.prev
            elif total < target:
                left = left.next
            else:
                right = right.prev

        return ans
        
    
