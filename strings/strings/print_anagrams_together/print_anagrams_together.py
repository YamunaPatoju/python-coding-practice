from collections import defaultdict

class Solution:
    def anagrams(self, arr):

        groups = defaultdict(list)

        for word in arr:
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values())
