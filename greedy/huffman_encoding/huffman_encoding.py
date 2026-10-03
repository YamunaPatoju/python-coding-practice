import heapq


class Node:
    def __init__(self, freq, index, left=None, right=None):
        self.freq = freq
        self.index = index
        self.left = left
        self.right = right


class Solution:
    def huffmanCodes(self, s, f):
        heap = []

        for i in range(len(s)):
            node = Node(f[i], i)
            heapq.heappush(heap, (f[i], i, node))

        if len(heap) == 1:
            return ["0"]

        while len(heap) > 1:
            freq1, index1, left = heapq.heappop(heap)
            freq2, index2, right = heapq.heappop(heap)

            new_node = Node(
                freq1 + freq2,
                min(index1, index2),
                left,
                right
            )

            heapq.heappush(
                heap,
                (new_node.freq, new_node.index, new_node)
            )

        root = heap[0][2]
        result = []

        def preorder(node, code):
            if node.left is None and node.right is None:
                result.append(code)
                return

            preorder(node.left, code + "0")
            preorder(node.right, code + "1")

        preorder(root, "")

        return result
