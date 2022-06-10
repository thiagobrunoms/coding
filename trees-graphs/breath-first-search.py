class Node:
    def __init__(self, value, neighbors: list) -> None:
        self.value = value
        self.neighbors = neighbors


class BFS:
    def __init__(self, visiting_nodes: list, starting_node: Node) -> None:
        self.visiting_nodes = visiting_nodes
        self.visited_nodes = []
        self.starting_node = starting_node

    def start_visiting(self):
        self.visiting_nodes.append(self.starting_node)

        while self.visiting_nodes:
            current_node: Node = self.visiting_nodes.pop(0)

            if current_node not in self.visited_nodes:
                print(current_node.value)
                self.visited_nodes.append(current_node)

            for neighbor in current_node.neighbors:
                if neighbor not in self.visited_nodes:
                    self.visiting_nodes.append(neighbor)

two = Node("2", [])
three = Node("3", [])
four = Node("4", [])
five = Node("5", [])
six = Node("6", [])
seven = Node("7", [])
eight = Node("8", [])

two.neighbors.extend([three])
three.neighbors.extend([four, five, two])
four.neighbors.extend([three, eight])
five.neighbors.extend([seven, three])
seven.neighbors.extend([five, eight])
eight.neighbors.extend([seven, four])

dfs = BFS([five, three, two, four, seven, eight], five)

dfs.start_visiting()