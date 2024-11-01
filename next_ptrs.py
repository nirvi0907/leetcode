
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # def dfs(node):
        #     if not node:
        #         return

        #     if node.left:
        #         node.left.next = node.right
        #         if node.next:
        #             if node.right:
        #                 node.right.next = node.next.left
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return root
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur,nxt=root,root.left if root else None
        while cur and nxt:
            cur.left.next=cur.right
            if cur.next:
                cur.right.next=cur.next.left
            cur=cur.next
            if not cur:
                cur=nxt
                nxt=cur.left
        return root

    class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Use bfs
        que = deque()
        que.append(root)
        while que and que[0]:
            length = len(que)
            for i in range(length):
                curr = que.popleft()
                curr.next = que[0] if i+1 < length else None
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                
        return root