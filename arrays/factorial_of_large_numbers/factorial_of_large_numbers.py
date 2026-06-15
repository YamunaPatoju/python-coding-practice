class Solution:
    def factorial(self, n):
        fact = 1

        for i in range(2, n + 1):
            fact *= i

        return [int(digit) for digit in str(fact)]
