# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]

class Node:
    def __init__(self, value, neighbors: list) -> None:
        self.value = value
        self.neighbors = neighbors

    def __str__(self):
        neighbors_str = ""
        for each_neighbor in self.neighbors:
            neighbors_str += each_neighbor.__str__()

        return '[value = ' + str(self.value) + ", neighbors = " + neighbors_str

class DFS:
    def __init__(self) -> None:
        self.start_node = None
        self.visited_nodes = set()
        self.visiting_nodes = []

    def findOrder(self, numCourses: int, prerequisites: list) -> list:
        prerequisites_dict = {}
        
        for pair in prerequisites:
            node0 = None
            node1 = None

            for each_node in prerequisites_dict.keys():
                if each_node.value == pair[0]:
                    node0 = each_node

                if each_node.value == pair[1]:
                    node1 = each_node

            if node0 == None:
                node0 = Node(pair[0], [])
            if node1 == None:
                node1 = Node(pair[1], [])

            node0.neighbors.append(node1)
            node1.neighbors.append(node0)

            prerequisites_dict[node0] = node0
            prerequisites_dict[node1] = node1

        # for each_node in prerequisites_dict.values():
        #     print('nó = ' + str(each_node.value))
        #     print('vizinhos: ')
        #     for each_neighbor in each_node.neighbors:
        #         print('no vizinho ' + str(each_neighbor.value))
        #         print('tamanho de vizinhos ' + str(len(each_neighbor.neighbors)))

        values_list = list(prerequisites_dict.values())
        self.start_node = values_list[1]
        self.start_visiting()

    def start_visiting(self):
        self.visiting_nodes.append(self.start_node)

        while self.visiting_nodes:
            current_node: Node = self.visiting_nodes.pop(0)

            if current_node not in self.visited_nodes:
                print(current_node.value)
                self.visited_nodes.add(current_node)

            for neighbor in current_node.neighbors:
                if neighbor not in self.visited_nodes:
                    self.visiting_nodes.append(neighbor)



bfs = DFS()
# course_order = bfs.start_visiting()
# print(course_order)
bfs.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])



        #    if pair[0] not in prerequisites_dict:
        #         neighbors = [Node(pair[1], [Node(pair[0], [])])]
        #         prerequisites_dict[pair[0]] = neighbors

                
        #         if pair[1] not in prerequisites_dict:
        #             neighbors = [Node(pair[0], [])]
        #             prerequisites_dict[pair[1]] = neighbors
        #         else:
        #             neighbors = prerequisites_dict[pair[1]]
        #             neighbors.append(Node(pair[0], []))
        #             prerequisites_dict[pair[1]] = neighbors
        #     else:
        #         neighbors = prerequisites_dict[pair[0]]
        #         neighbors.append(Node(pair[1], []))
        #         prerequisites_dict[pair[0]] = neighbors

        #         if pair[1] not in prerequisites_dict:
        #             neighbors = [Node(pair[0], [])]
        #             prerequisites_dict[pair[1]] = neighbors
        #         else:
        #             neighbors = prerequisites_dict[pair[1]]
        #             neighbors.append(Node(pair[0], []))
        #             prerequisites_dict[pair[1]] = neighbors

        # all_elements = []
        # for values in prerequisites_dict.values():
        #     all_elements.extend(values)

        # self.start_node = all_elements[0]