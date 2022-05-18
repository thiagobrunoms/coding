from inspect import stack


class FixedSizeThreeStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.number_of_stacks = 3
        self.stack_sizes = [0, 0, 0]
        self.stack_values = [None for i in range(self.capacity * self.number_of_stacks)]

    def push(self, stack_index, value):
        if self.is_full(stack_index):
            print('Não pode mais adicionar na stack', stack_index)
            return

        self.stack_sizes[stack_index] += 1

        stack_top_index = self.get_stack_top_index(stack_index)
        self.stack_values[stack_top_index] = value
        print(self.stack_values)

    def pop(self, stack_index):
        if self.is_empty(stack_index):
            return 
            
        stack_top_index = self.get_stack_top_index(stack_index)
        self.stack_values[stack_top_index] = None
        self.stack_sizes[stack_index] -= 1
        print(self.stack_values)

    def peek(self, stack_index):
        index = self.get_stack_top_index(stack_index)
        return self.stack_values[index]


    def get_stack_top_index(self, stack_index):
        offset = stack_index * self.capacity
        number_of_elements = self.stack_sizes[stack_index]

        return offset + number_of_elements - 1

    def is_full(self, stack_index):
        return self.stack_sizes[stack_index] == self.capacity

    def is_empty(self, stack_index):
        return self.stack_sizes[stack_index] == 0

stack3 = FixedSizeThreeStack(10)
stack3.push(0, 5)
stack3.push(1, 11)
stack3.push(2, 222)
stack3.push(1, 12)
stack3.push(1, 13)
stack3.push(1, 14)
stack3.push(1, 15)
stack3.push(1, 16)
stack3.push(1, 17)
stack3.push(1, 18)
stack3.push(1, 19)
stack3.push(1, 20)
stack3.push(1, 21)
stack3.push(1, 22)
stack3.push(2, 223)
# stack3.pop(1)
# stack3.pop(1)
# stack3.pop(1)
# stack3.pop(1)
# stack3.pop(1)
# stack3.pop(1)
# stack3.pop(1)
print(stack3.peek(1))

