from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BFS:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:return []
        res = []
        q = deque([(root, 0)])
        while q:
            node, depth = q.popleft()
            if depth == len(res):
                res.append(0)
            res[depth] = node.val
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        return res

class DFS:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:return []
        res = []
        def dfs(root, depth):
            nonlocal res
            ## base
            if not root:
                return
            
            ## body
            if len(res) == depth:
                res.append(0)
            res[depth] = root.val
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        
        dfs(root, 0)
        return res