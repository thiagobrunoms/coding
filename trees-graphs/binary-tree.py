
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTreeNode(value)
            else:
                self.right.insert(value)

    def in_order_traversal(self, node):
        if (node):
            self.in_order_traversal(node.left)
            print(node.value)
            self.in_order_traversal(node.right)

binaryTree = BinaryTreeNode(10)
binaryTree.insert(7)
binaryTree.insert(12)
binaryTree.insert(5)
binaryTree.insert(6)
binaryTree.insert(11)
binaryTree.insert(13) 

binaryTree.in_order_traversal(binaryTree)