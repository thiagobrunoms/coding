class StringBuilder:
    def __init__(self, chars_sequence = None):
        self.current_len = 0

        if chars_sequence == None:
            self.content = [None for i in range(16)]
        else:
            self.current_len = len(chars_sequence)
            self.content = [s for s in chars_sequence]
            self.content.extend([None for i in range(len(chars_sequence))])

    def append(self, chars_sequence):
        self.__ensure_capacity(chars_sequence)
        for i in range(len(chars_sequence)):
            self.content[self.current_len] = chars_sequence[i]
            self.current_len = self.current_len + 1

        self.current_len = self.current_len + 1 #space between append calls 
        

        print("current len", self.current_len)
        print("sentence", self.content)
        print("buffer size", len(self.content))
        
    def __ensure_capacity(self, chars_sequence):
        if len(chars_sequence) + self.current_len > len(self.content) * 0.8:
            self.content.extend([None for i in range(len(self.content) // 2) ])
        
    
    def __str__(self):
        string = ""
        for s in self.content:
            if s != None:
                string = string + s
            else:
                string += " "                

        return string.strip() 
        


string_builder = StringBuilder()
string_builder.append("Thiago")
string_builder.append("Bruno")
string_builder.append("Melo")
string_builder.append("de")
string_builder.append("Sales")
print(string_builder)      
print(len(string_builder.__str__()))      