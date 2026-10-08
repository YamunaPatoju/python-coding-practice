class Solution:
    def minCashFlow(self, transaction):
        n = len(transaction)

        balance = [0] * n

        for i in range(n):
            for j in range(n):
                balance[i] -= transaction[i][j]
                balance[j] += transaction[i][j]

        result = [[0] * n for _ in range(n)]

        while True:
            debtor = -1
            creditor = -1

            for i in range(n):
                if balance[i] < 0:
                    if debtor == -1 or balance[i] < balance[debtor]:
                        debtor = i

                if balance[i] > 0:
                    if creditor == -1 or balance[i] > balance[creditor]:
                        creditor = i

            if debtor == -1 or creditor == -1:
                break

            amount = min(-balance[debtor], balance[creditor])

            result[debtor][creditor] = amount

            balance[debtor] += amount
            balance[creditor] -= amount

        return result
