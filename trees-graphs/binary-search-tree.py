class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.left: Node = None
        self.right: Node = None

    
class BinarySearchTree:

    def insert(self, value: int, root: Node) -> Node:
        if root == None:
            root = Node(value)
            return root

        if value == root.value:
            return root

        if value < root.value:
            root.left = self.insert(value, root.left)
        else:
            root.right = self.insert(value, root.right)

        return root

    def pre_order_traversall(self, root: Node, elements: list):
        if root != None:
            elements.append(root.value)
            self.pre_order_traversall(root.left, elements)
            self.pre_order_traversall(root.right, elements)

        return elements

    def in_order_traversall(self, root: Node, elements: list):
        if root != None:
            self.in_order_traversall(root.left, elements)
            elements.append(root.value)
            self.in_order_traversall(root.right, elements)

        return elements

    def post_order_traversall(self, root: Node, elements: list):
        if root != None:
            self.post_order_traversall(root.left, elements)
            self.post_order_traversall(root.right, elements)
            elements.append(root.value)

        return elements

    

bst = BinarySearchTree()
root = bst.insert(27, None)
root = bst.insert(14, root)
root = bst.insert(35, root)
root = bst.insert(10, root)
root = bst.insert(19, root)
root = bst.insert(31, root)
root = bst.insert(42, root)

# print(root.value)
# print(root.right.right.value)
# print(root.left.left.value)

#in-order
print("pre-order traversal")
elements = []
elements = bst.pre_order_traversall(root, elements)
print(elements)

print("In-order traversal")
elements = []
elements = bst.in_order_traversall(root, elements)
print(elements)

print("Post-order traversal")
elements = []
elements = bst.post_order_traversall(root, elements)
print(elements)