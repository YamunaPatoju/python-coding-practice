class Solution:
    def multiplyTwoLists(self, first, second):
        mod = 1000000007

        num1 = 0
        num2 = 0

        while first:
            num1 = (num1 * 10 + first.data) % mod
            first = first.next

        while second:
            num2 = (num2 * 10 + second.data) % mod
            second = second.next

        return (num1 * num2) % mod
