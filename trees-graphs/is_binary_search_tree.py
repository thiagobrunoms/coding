class Node:
    def __init__(self, value):
        self.value = value
        self.left: Node = None
        self.right: Node = None

class BST:
    def is_bst(self, root: Node) -> bool:
        if root.left != None and root.left.value > root.value:
            return False

        if root.right != None and root.right.value < root.value:
            return False

        if not self.is_bst(root.left) or not self.is_bst(root.right):
            return False

        return True