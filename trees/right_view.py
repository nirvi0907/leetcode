class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # rv = []
        # def fill_right_view(node, level):
        #     if not node:
        #         return
        #     if len(rv)==level:
        #         rv.append(node.val)
        #     fill_right_view(node.right, level+1)
        #     fill_right_view(node.left, level+1)
        
        # fill_right_view(root, 0)

        # return rv
        
        
        rv = []
        if root:
            stack = [(root, 0)]
            while stack:
                node, level = stack.pop()
                if level==len(rv):
                    rv.append(node.val)
                if node.left:
                    stack.append((node.left, level+1))
                if node.right:
                    stack.append((node.right, level+1))
        return rv