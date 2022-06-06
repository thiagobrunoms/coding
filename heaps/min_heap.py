import math

class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.size = 0

    def get_left_item_index(self, index) -> int:
        return index * 2 + 1
    def get_right_item_index(self, index) -> int:
        return index * 2 + 2
    def get_parent_item_index(self, index) -> int:
        return math.ceil((index - 2) / 2)

    def get_left_item(self, index) -> int:
        return self.items[self.get_left_item_index(index)]
    def get_right_item(self, index) -> int:
        return self.items[self.get_right_item_index(index)]
    def get_parent_item(self, index) -> int:
        return self.items[self.get_parent_item_index(index)]

    def has_left_child(self, index):
        return self.get_left_item_index(index) < self.size
    def has_right_child(self, index):
        return self.get_right_item_index(index) < self.size
    def has_parent(self, index):
        return self.get_parent_item_index(index) >= 0

    def swap_elements(self, index1, index2): 
        temp = self.items[index1]
        self.items[index1] = self.items[index2]
        self.items[index2] = temp

    def has_elements(self) -> bool:
        return self.size > 0
    
    def peek(self) -> int:
        if not self.has_elements():
            raise Exception('Illegal!')

        return self.items[0]

    def ensure_capacity(self):
        if self.size >= len(self.items) * 0.7:
            new_items = [None] * len(self.items)
            self.items = self.items.extend(new_items)

    def poll(self) -> int:
        if not self.has_elements():
            raise Exception('Illegal!')

        item = self.items[0]

        self.items[0] = self.items[self.size - 1]
        self.items[self.size - 1] = None
        self.size -= 1

        self.heapfy_down()

        return item

    def add_item(self, item):
        self.ensure_capacity()
        self.items[self.size] = item
        self.size += 1
        print(self.items)
        self.heapfy_up()

    def heapfy_down(self):
        index = 0
        while self.has_left_child(index) and self.has_right_child(index):
            if self.get_left_item(index) < self.get_right_item(index):
                self.swap_elements(self.get_left_item_index(index), index)
                index = self.get_left_item_index(index)
            else:
                self.swap_elements(self.get_right_item_index(index), index)
                index = self.get_right_item_index(index)


    def heapfy_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.get_parent_item(index) > self.items[index]:
            self.swap_elements(self.get_parent_item_index(index), index)
            index = self.get_parent_item_index(index)

    def show(self):
        print(self.items)


min_heap = MinHeap(10)
min_heap.add_item(10)
min_heap.add_item(15)
min_heap.add_item(20)
min_heap.add_item(17)
min_heap.add_item(8)
min_heap.add_item(2)
print('tree as array')
min_heap.show()
min_heap.poll()
min_heap.show()
min_heap.poll()
min_heap.show()
min_heap.poll()
min_heap.show()
# print('peek', min_heap.peek())