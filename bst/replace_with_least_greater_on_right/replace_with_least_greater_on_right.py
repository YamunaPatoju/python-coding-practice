class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def findLeastGreater(self, arr):
        root = None
        result = [-1] * len(arr)

        def insert(node, value):
            if node is None:
                return Node(value)

            if value < node.data:
                node.left = insert(node.left, value)
            else:
                node.right = insert(node.right, value)

            return node

        def find_successor(node, value):
            successor = None

            while node:
                if node.data > value:
                    successor = node
                    node = node.left
                else:
                    node = node.right

            return successor.data if successor else -1

        for i in range(len(arr) - 1, -1, -1):
            result[i] = find_successor(root, arr[i])
            root = insert(root, arr[i])

        return result
