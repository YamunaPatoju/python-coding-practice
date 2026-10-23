t = int(input())

for _ in range(t):
    w, h, n = map(int, input().split())

    x_positions = [0, w + 1]
    y_positions = [0, h + 1]

    for _ in range(n):
        x, y = map(int, input().split())
        x_positions.append(x)
        y_positions.append(y)

    x_positions.sort()
    y_positions.sort()

    max_width = 0
    max_height = 0

    for i in range(1, len(x_positions)):
        max_width = max(
            max_width,
            x_positions[i] - x_positions[i - 1] - 1
        )

    for i in range(1, len(y_positions)):
        max_height = max(
            max_height,
            y_positions[i] - y_positions[i - 1] - 1
        )

    print(max_width * max_height)
