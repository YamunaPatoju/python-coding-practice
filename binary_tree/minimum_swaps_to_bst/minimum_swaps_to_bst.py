def inorder(arr, result, index):
    n = len(arr)

    if index >= n:
        return

    inorder(arr, result, 2 * index + 1)
    result.append(arr[index])
    inorder(arr, result, 2 * index + 2)


class Solution:
    def minSwaps(self, arr):
        inorder_arr = []
        inorder(arr, inorder_arr, 0)

        pairs = [(value, index) for index, value in enumerate(inorder_arr)]
        pairs.sort()

        n = len(pairs)
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pairs[i][1] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pairs[j][1]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps
