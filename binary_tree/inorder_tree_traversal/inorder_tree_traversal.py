def inorder_recursive(root):
    result = []

    def traverse(node):
        if node is None:
            return

        traverse(node.left)
        result.append(node.data)
        traverse(node.right)

    traverse(root)
    return result


def inorder_iterative(root):
    result = []
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        result.append(curr.data)
        curr = curr.right

    return result
