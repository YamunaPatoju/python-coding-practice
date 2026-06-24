class Solution:
    def commonElements(self, mat):
        rows = len(mat)

        common = set(mat[0])

        for i in range(1, rows):
            common = common.intersection(set(mat[i]))

        return list(common)
