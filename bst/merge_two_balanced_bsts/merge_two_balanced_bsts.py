class Solution:
    def mergeTrees(self, root1, root2, m, n):
        arr1 = []
        arr2 = []

        def inorder(node, arr):
            if node is None:
                return

            inorder(node.left, arr)
            arr.append(node.data)
            inorder(node.right, arr)

        inorder(root1, arr1)
        inorder(root2, arr2)

        merged = []
        i = 0
        j = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1

        while i < len(arr1):
            merged.append(arr1[i])
            i += 1

        while j < len(arr2):
            merged.append(arr2[j])
            j += 1

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = Node(merged[mid])

            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        return build(0, len(merged) - 1)
