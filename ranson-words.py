class Solution:
    def check_ranson_words(self, sentence_s1 , sentence_s2):
        sentence_structure = set()
        seen = set()

        sentence_s1_words = sentence_s1.split(" ")
        sentence_s2_words = sentence_s2.split(" ")

        for s1 in sentence_s1_words:
            sentence_structure.add(s1)
            
        for s2 in sentence_s2_words:
            if s2 not in sentence_structure or s2 in seen: 
                return False

            seen.add(s2)

        return True

# sentence_s1 = "give me one grand today night"
# sentence_s2 = "give one grand today"

sentence_s1 = "two times three is not four"
sentence_s2 = "two times two is four"

s  = Solution()
result = s.check_ranson_words(sentence_s1, sentence_s2)
print(result)