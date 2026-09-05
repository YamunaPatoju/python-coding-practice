class Solution:
    def treeFromString(self, s):
        if not s:
            return None

        def build(i):
         
            num = 0

            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1

            node = Node(num)

        
            if i < len(s) and s[i] == '(':
                i += 1

              
                if s[i] != ')':
                    node.left, i = build(i)

                i += 1

            if i < len(s) and s[i] == '(':
                i += 1

                if s[i] != ')':
                    node.right, i = build(i)

                i += 1

            return node, i

        root, _ = build(0)
        return root
