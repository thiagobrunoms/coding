

# EXAPLANTION BASED: https://www.youtube.com/watch?v=vXrv3kruvwE

# flag -1: non-visited node
# flag 0: node is to be visited (in the queue)
# flag 1: node has been visited

class Node:
    def __init__(self, value, neighbors: list):
        self.value = value
        self.neighbors = neighbors
        self.flag = -1


class DetectCycleBFS:
    def __init__(self, start_node: Node):
        self.to_visit = []
        self.start_node = start_node
        self.visited_nodes = []

    def has_cycle(self) -> bool:
        self.to_visit.append(self.start_node)
        self.start_node.flag = 0

        while self.to_visit:
            current_node: Node = self.to_visit.pop(0)

            if current_node not in self.visited_nodes:
                print(current_node.value)
                current_node.flag = 1
                self.visited_nodes.append(current_node)

            for neighbor in current_node.neighbors:
                if neighbor not in self.visited_nodes:
                    if neighbor.flag == 0:
                        return True
                    else:
                        neighbor.flag = 0
                        self.to_visit.append(neighbor)

        return False


# ===== IT HAS A CYCLE - EXAMPLE ======
two = Node("2", [])
three = Node("3", [])
four = Node("4", [])
five = Node("5", [])
six = Node("6", [])
seven = Node("7", [])

two.neighbors.extend([three, four])
three.neighbors.extend([five, six])
four.neighbors.extend([seven])
six.neighbors.extend([seven])

dfs = DetectCycleBFS(two)

has_cycle = dfs.has_cycle()
if has_cycle:
    print('It has a cycle')
else:
    print('It does not have a cycle')

# ===== IT DOES NOT HAVE A CYCLE - EXAMPLE ======

two = Node("2", [])
three = Node("3", [])
four = Node("4", [])
five = Node("5", [])
six = Node("6", [])
seven = Node("7", [])

two.neighbors.extend([three, four])
four.neighbors.extend([five])
five.neighbors.extend([six, seven])

dfs = DetectCycleBFS(two)

has_cycle = dfs.has_cycle()
if has_cycle:
    print('It has a cycle')
else:
    print('It does not have a cycle')
