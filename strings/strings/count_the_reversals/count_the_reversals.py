def countminreversals(s):

    n = len(s)

    if n % 2 != 0:
        return -1

    stack = []

    for ch in s:
        if ch == '{':
            stack.append(ch)
        else:
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(ch)

    open_braces = 0
    close_braces = 0

    while stack:
        if stack.pop() == '{':
            open_braces += 1
        else:
            close_braces += 1

    return (open_braces + 1) // 2 + (close_braces + 1) // 2
