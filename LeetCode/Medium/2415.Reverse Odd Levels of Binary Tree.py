from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        level = 0

        while queue:
            current = []
            for _ in range(len(queue)):
                node = queue.popleft()
                current.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 1: #홀수 레벨일 경우
                for i in range(len(current)//2):
                    current[i].val, current[~i].val = current[~i].val, current[i].val
            level += 1
        
        return root
