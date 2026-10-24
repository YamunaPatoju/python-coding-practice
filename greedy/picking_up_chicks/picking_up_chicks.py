t = int(input())

for case in range(1, t + 1):
    N, K, B, T = map(int, input().split())
    X = list(map(int, input().split()))
    V = list(map(int, input().split()))

    if K == 0:
        print(f"Case #{case}: 0")
        continue

    swaps = 0
    slow_chicks = 0
    reached = 0

    for i in range(N - 1, -1, -1):
        distance = B - X[i]

        if V[i] * T >= distance:
            reached += 1
            swaps += slow_chicks

            if reached == K:
                break
        else:
            slow_chicks += 1

    if reached < K:
        print(f"Case #{case}: IMPOSSIBLE")
    else:
        print(f"Case #{case}: {swaps}")
