
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None

    def insert(self, value):
        print('adding', value, 'where self.left', self.left.value if self.left and self.left.value is not None else 'None', 'and self.right', self.right.value if self.right and self.right.value is not None else 'None')

        if value < self.value:
            if self.left is None:
                self.left = BinaryTreeNode(value)
                print('added ', value, 'as left from')
            else:
                print('recursing left', self.left.value)
                self.left.insert(value)
        else:
            if self.right is None:
                print('added ', value, 'as right ')
                self.right = BinaryTreeNode(value)
            else:
                print('recursing right', self.right.value)
                self.right.insert(value)

    def in_order_traversal(self, node):
        if (node):
            self.in_order_traversal(node.left)
            print(node.value)
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if (node):
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.value)

    def pre_order_traversal(self, node):
        if (node):
            print(node.value)
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

binaryTree = BinaryTreeNode(10)
binaryTree.insert(5)
binaryTree.insert(13)
binaryTree.insert(6)
binaryTree.insert(7)
binaryTree.insert(11)
binaryTree.insert(12) 

print('in order traversal - as left as possible - left -> root -> right')
binaryTree.in_order_traversal(binaryTree)

print('post order traversal -> left -> right -> root')
binaryTree.post_order_traversal(binaryTree)

print('pre order traversal -> root -> left -> right')
binaryTree.pre_order_traversal(binaryTree)