def print_sentences(arr):

    result = []

    def dfs(index, path):

        if index == len(arr):
            result.append(" ".join(path))
            return

        for word in arr[index]:
            dfs(index + 1, path + [word])

    dfs(0, [])

    return result


arr = [
    ["you", "we"],
    ["have", "are"],
    ["sleep", "eat", "drink"]
]

for sentence in print_sentences(arr):
    print(sentence)
