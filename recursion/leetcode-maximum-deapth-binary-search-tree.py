# Definition for a binary tree node.
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        left_value: TreeNode = root.left
        right_value: TreeNode = root.right

        biggest = max(self.maxDepth(left_value), self.maxDepth(right_value))
        print(biggest)
        return 1 + biggest


t8 = TreeNode(8)
t7 = TreeNode(5, right=t8)
t6 = TreeNode(6)
t5 = TreeNode(5)
t4 = TreeNode(4)
t3 = TreeNode(3, t6, t7)
t2 = TreeNode(2, t4, t5)
t1 = TreeNode(1, t2, t3)

s = Solution()
result = s.maxDepth(t1)
print(result)
