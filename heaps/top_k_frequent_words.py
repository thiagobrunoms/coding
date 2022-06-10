import math
class Item:
    def __init__(self, word: str):
        self.word = word
        self.count = 1

    def __str__(self):
        return "[word = " + self.word + ", count = " + str(self.count) + "]"

class Solution:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.size = 0
        
    def topKFrequent(self, words: list, k: int) -> list:
        for element in words:
            self.add_item(Item(element))

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

    def ensure_capacity(self):
        if self.size >= len(self.items) * 0.7:
            new_items = [None] * len(self.items)
            self.items = self.items.extend(new_items)

    def add_item(self, item: Item):
        print('Adicionando ', item.word)
        self.ensure_capacity()
        self.items[self.size] = item
        self.size += 1
        self.heapfy_up()

    def heapfy_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.get_parent_item(index).count <= self.items[index].count:
            # print('index', index, 'parent index', self.get_parent_item_index(index), " -> ", self.get_parent_item(index))
            print(self.__str__())
            if self.get_parent_item(index).word == self.items[index].word:
                self.size -= 1
                self.get_parent_item(index).count += 1
                if self.get_parent_item(self.get_parent_item_index(index)).count < self.get_parent_item(index).count:
                    self.swap_elements(self.get_parent_item_index(self.get_parent_item_index(index)), self.get_parent_item_index(index))
                    print('trocou com avo')
                continue

            self.swap_elements(self.get_parent_item_index(index), index)
            index = self.get_parent_item_index(index)

    def __str__(self):
        content = ""
        for item in self.items:
            content += item.__str__() + ", "

        return content
            

# words = ["i","love","leetcode","i","love","coding"]        
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
s = Solution(len(words))
s.topKFrequent(words, 2)
print(s)