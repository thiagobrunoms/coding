class Node:
    def __init__(self, value, neighbors: list) -> None:
        self.value = value
        self.neighbors = neighbors


class BFS:
    def __init__(self,  starting_node: Node) -> None:
        self.starting_node = starting_node
        self.visited_nodes = set()
        self.visiting_nodes = []

    def start_visiting(self):
        print('initing', self.visiting_nodes)
        self.visiting_nodes.append(self.starting_node)

        while self.visiting_nodes:
            current_node: Node = self.visiting_nodes.pop(0)  # Queue

            if current_node not in self.visited_nodes:
                print(current_node.value)
                self.visited_nodes.add(current_node)

            for neighbor in current_node.neighbors:
                if neighbor not in self.visited_nodes:
                    self.visiting_nodes.append(neighbor)

class NodeBST:
    def __init__(self, value):
        self.value = value
        self.left: NodeBST = None
        self.right: NodeBST = None
class BFSInBSTree:
    def __init__(self, root: NodeBST):
        self.visiting_nodes = [root]

    def start_searching(self):
        while len(self.visiting_nodes) > 0:
            current = self.visiting_nodes.pop(0)
            print(current)
            if current.left is not None:
                self.visiting_nodes.append(current.left)
            if current.right is not None:
                self.visiting_nodes.append(current.right)
            

    

# two = Node("2", [])
# three = Node("3", [])
# four = Node("4", [])
# five = Node("5", [])
# six = Node("6", [])
# seven = Node("7", [])
# eight = Node("8", [])

# two.neighbors.extend([three])
# three.neighbors.extend([four, five, two])
# four.neighbors.extend([three, eight])
# five.neighbors.extend([seven, three])
# seven.neighbors.extend([five, eight])
# eight.neighbors.extend([seven, four])

# dfs = BFS([five, three, two, four, seven, eight], five)


two = Node("2", [])
three = Node("3", [])
four = Node("4", [])
five = Node("5", [])
six = Node("6", [])
seven = Node("7", [])
# eight = Node("8", [])

two.neighbors.extend([three, four])
three.neighbors.extend([five, six])
four.neighbors.extend([seven])
six.neighbors.extend([seven])


dfs = BFS(two)

dfs.start_visiting()
