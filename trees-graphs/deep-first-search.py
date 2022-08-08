class Node:
    def __init__(self, value, neighbors: list) -> None:
        self.value = value
        self.neighbors = neighbors


class DFS:
    def __init__(self, start_node: Node) -> None:
        self.start_node = start_node
        self.visited_nodes = set()
        self.visiting_nodes = []

    def start_visiting(self):
        self.visiting_nodes.append(self.start_node)

        while self.visiting_nodes:
            current_node: Node = self.visiting_nodes.pop()  # Stack

            if current_node not in self.visited_nodes:
                print(current_node.value)
                self.visited_nodes.add(current_node)

            for neighbor in current_node.neighbors:
                if neighbor not in self.visited_nodes:
                    self.visiting_nodes.append(neighbor)


# B = Node("B", [])
# C = Node("C", [])
# D = Node("D", [])
# E = Node("E", [])
# F = Node("F", [])
# G = Node("G", [])
# H = Node("H", [])

# A = Node("A", [B, C, D, E])
# B.neighbors.extend([G, C, A])
# C.neighbors.extend([B, A, D])
# D.neighbors.extend([C, A, E, H])
# E.neighbors.extend([A, D, F])
# F.neighbors.extend([G, H, E])
# G.neighbors.extend([B, F])
# H.neighbors.extend([F, D])

# dfs = DFS([A, B, C, D, E, F, G, H], A)

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

dfs = DFS(five)

dfs.start_visiting()
