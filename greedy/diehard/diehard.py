def max_survival_time(H, A):
    def solve(health, armor, place):
        if health <= 0 or armor <= 0:
            return 0

        if place == "air":
            health += 3
            armor += 2
        elif place == "water":
            health -= 5
            armor -= 10
        else:
            health -= 20
            armor += 5

        if health <= 0 or armor <= 0:
            return 0

        if place == "air":
            return 1 + max(
                solve(health, armor, "water"),
                solve(health, armor, "fire")
            )

        if place == "water":
            return 1 + max(
                solve(health, armor, "air"),
                solve(health, armor, "fire")
            )

        return 1 + max(
            solve(health, armor, "air"),
            solve(health, armor, "water")
        )

    return max(
        solve(H, A, "air"),
        solve(H, A, "water"),
        solve(H, A, "fire")
    )


t = int(input())

for _ in range(t):
    H, A = map(int, input().split())
    print(max_survival_time(H, A))
