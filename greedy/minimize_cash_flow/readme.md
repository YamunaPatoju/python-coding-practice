# Minimize Cash Flow

## Problem

Given `n` friends and a transaction matrix, where `transaction[i][j]` represents the amount of money friend `i` owes to friend `j`, find a settlement that minimizes the total cash flow.

The settlement must:

* Preserve the same net balance for every friend.
* Have only non-negative payments.
* Have `0` on the diagonal.
* Minimize the total amount of money transferred.

## Approach

Use a **Greedy** approach.

First calculate the net balance of every friend:

* Negative balance → friend needs to pay money.
* Positive balance → friend needs to receive money.
* Zero balance → no payment is required.

Then repeatedly:

1. Find the friend who owes the most money.
2. Find the friend who should receive the most money.
3. Transfer the minimum of the two amounts.
4. Update their balances.
5. Continue until all balances become zero.

## Algorithm

1. Create a `balance` array initialized to zero.
2. For every transaction:

   * Subtract the amount from the payer's balance.
   * Add the amount to the receiver's balance.
3. Create an empty result matrix.
4. Find the largest debtor and largest creditor.
5. Transfer:
   `min(debt, credit)`
6. Update both balances.
7. Repeat until there are no debtors or creditors.
8. Return the settlement matrix.

## Example

### Input

```text
transaction = [
    [0, 100, 0],
    [0, 0, 200],
    [0, 0, 0]
]
```

Net balances:

```text
Friend
```
