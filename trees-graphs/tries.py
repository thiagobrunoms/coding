class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {} #key: char, #value: reference to another TrieNode

    def __str__(self):
        return "char = " + self.char + ", is_ending = " + str(self.is_end) + ", children = " + self.children.__str__()

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert_word(self, word: str):
        current = self.root

        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode(letter)
            
            print(current.char, " -> ", current)
            current = current.children[letter]

        current.is_end = True

    def autocomplete(self, prefix: str):
        suggestions = []
        
        current = self.root
        for letter in prefix:
            if letter in current.children:
                current = current.children[letter]
            else:
                return suggestions

        if current.is_end:
            suggestions.append(prefix)
            
        self.lookup_suggestions(current, prefix, suggestions)
        return suggestions

    def lookup_suggestions(self, current: TrieNode, prefix: str, suggestions: list) -> list:
        if current.children:
            for char in current.children:
                suggestion_word = prefix + char

                if current.children[char].is_end:
                    suggestions.append(suggestion_word)
                
            current = current.children[char]
            self.lookup_suggestions(current, suggestion_word, suggestions)

    def __str__(self):
        return self.root

suggestions = Trie()
suggestions.insert_word("word")
suggestions.insert_word("work")
suggestions.insert_word("working") #it is not been suggested! why?
suggestions.insert_word("worring")

suggestions_list = suggestions.autocomplete("wor")
print(suggestions_list)