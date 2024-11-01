class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.depth = 0
        self.lca = None
        self.dfs(root, 0)
        return self.lca
    
    def dfs(self, cur, depth):
        if cur is None:
           return depth

        left = self.dfs(cur.left, depth+1)
        right = self.dfs(cur.right, depth+1)

        depth = max(left, right)
        self.depth = max(self.depth, depth)

        if left == right == self.depth:
           self.lca = cur 

        return depth