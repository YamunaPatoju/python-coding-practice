class Solution:
    def findPreSuc(self, root, key):
        predecessor = None
        successor = None

        current = root

        while current:
            if current.data < key:
                predecessor = current
                current = current.right

            elif current.data > key:
                successor = current
                current = current.left

            else:
                if current.left:
                    temp = current.left

                    while temp.right:
                        temp = temp.right

                    predecessor = temp

                if current.right:
                    temp = current.right

                    while temp.left:
                        temp = temp.left

                    successor = temp

                break

        return predecessor, successor
