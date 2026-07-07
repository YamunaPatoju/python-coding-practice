def firstRepeatedWord(s):

    words = s.split()

    seen = set()

    ans = None

    for word in reversed(words):
        if word in seen:
            ans = word
        else:
            seen.add(word)

    return ans if ans else "No Repetition"


s = "Ravi had been saying that he had been there"
print(firstRepeatedWord(s))
