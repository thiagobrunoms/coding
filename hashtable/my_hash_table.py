from linked_list import *


class MyHashTable:
    def __init__(self):
        self.capacity = 10
        self.items: LinkedList = [None] * self.capacity
        self.size = 0

    def __calculate_bucket(self, item):
        item_hash = hash(item)
        bucket = item_hash % len(self.items)
        return bucket

    def put(self, key, value):
        self.__ensure_capacity()

        item: Node = Node(key, value)
        bucket = self.__calculate_bucket(item)
        if self.items[bucket] != None:
            bucket_list: LinkedList = self.items[bucket]
            bucket_list.insert(item)
        else:
            bucket_list = LinkedList(item)
            self.items[bucket] = bucket_list

        self.size += 1

    def __ensure_capacity(self):
        if self.size == self.size * 0.7:
            self.capacity += 10
            temp = [None] * self.capacity
            for items in self.items:
                temp.append(items)

            self.items = temp

    def delete(self, value) -> bool:
        bucket = self.__calculate_bucket(value)
        bucket_list: LinkedList = self.items[bucket]
        if bucket_list == None:
            return False

        bucket_list.delete(Node(value))
        self.size -= 1

    def show(self):
        print(self.items)
        for item in self.items:
            if item != None:
                print(item.show())


s = MyHashTable()
for i in range(20):
    s.put(i, i * 100)
s.show()
