
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left: BinaryTree = None
        self.right: BinaryTree = None

    def insert(self, value):
        node = BinaryTree(value)

        if node.value < value:
            if self.left is None:
                self.left = node
            else:
                self.insert_left(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.insert_right(node)

    def insert_left(self, node):
        node.left = self.left
        self.left = node

    def insert_right(self, node):
        node.right = self.right
        self.right = node

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()

        print(self.value)

        if self.right:
            self.right.in_order_traversal()

binaryTree = BinaryTree(10)
binaryTree.insert(7)
binaryTree.insert(12)
binaryTree.insert(5)            

binaryTree.in_order_traversal()
