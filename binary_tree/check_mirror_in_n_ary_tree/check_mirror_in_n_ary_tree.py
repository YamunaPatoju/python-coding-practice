class Solution:
    def checkMirrorTree(self, e, A, B):
        tree1 = [[] for _ in range(e + 2)]
        tree2 = [[] for _ in range(e + 2)]

        for i in range(0, 2 * e, 2):
            u = A[i]
            v = A[i + 1]
            tree1[u].append(v)

            u = B[i]
            v = B[i + 1]
            tree2[u].append(v)

        for i in range(1, e + 2):
            if tree1[i] != tree2[i][::-1]:
                return False

        return True
