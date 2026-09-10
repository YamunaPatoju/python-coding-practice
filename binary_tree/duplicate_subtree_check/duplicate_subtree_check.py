class Solution:
    def dupSub(self, root):
        subtrees = set()

        def dfs(node):
            if node is None:
                return "#"

            left = dfs(node.left)
            right = dfs(node.right)

            current = str(node.data) + "," + left + "," + right

            if left == "#" and right == "#":
                return current

            if current in subtrees:
                self.found = True

            subtrees.add(current)

            return current

        self.found = False
        dfs(root)

        return self.found
