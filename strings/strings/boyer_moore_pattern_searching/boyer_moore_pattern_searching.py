NO_OF_CHARS = 256


def badCharHeuristic(pattern):
    badChar = [-1] * NO_OF_CHARS

    for i in range(len(pattern)):
        badChar[ord(pattern[i])] = i

    return badChar


def boyerMooreSearch(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return []

    badChar = badCharHeuristic(pattern)

    result = []
    shift = 0

    while shift <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            result.append(shift)

            if shift + m < n:
                shift += m - badChar[ord(text[shift + m])]
            else:
                shift += 1
        else:
            shift += max(1, j - badChar[ord(text[shift + j])])

    return result


text = "AABAACAADAABAABA"
pattern = "AABA"

print(boyerMooreSearch(text, pattern))
