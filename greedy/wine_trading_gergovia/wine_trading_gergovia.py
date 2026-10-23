while True:
    n = int(input())

    if n == 0:
        break

    arr = list(map(int, input().split()))

    balance = 0
    work = 0

    for amount in arr:
        balance += amount
        work += abs(balance)

    print(work)
