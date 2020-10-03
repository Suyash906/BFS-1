# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BFS:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        
        q = deque([root])
        res = []
        
        while q:
            size = len(q)
            curr = []
            while size > 0:
                node = q.popleft()
                curr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size-=1
            res.append(curr)
        return res

class DFS:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(root, depth):
            nonlocal res
            ## base
            if not root:
                return
            
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root, 0)
        return res        