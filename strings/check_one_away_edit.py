from cgitb import small


class Solution:
    def check_one_away(self, word1: str, word2: str) -> bool:
        if len(word1) == len(word2):
            return self.check_replacement(word1, word2)
        elif len(word1) + 1 == len(word2):
            return self.check_Insertion_removal(word1, word2)
        elif len(word1) - 1 == len(word2):
            return self.check_Insertion_removal(word1, word2)
        return False

    def check_replacement(self, word1, word2):
        found_difference = False
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                if found_difference:
                    return False
                else:
                    found_difference = True

        return True


    def check_Insertion_removal(self, word1, word2) -> True:
        if len(word1) >= len(word2):
            bigger = word1
            smaller = word2
        else:
            bigger = word2
            smaller == word1

        index_smaller = 0
        index_bigger = 0
        found = False
        print(len(smaller))
        print(len(bigger))
        while index_smaller < len(smaller) and index_bigger < len(bigger):
            if smaller[index_smaller] != bigger[index_bigger]:
                if found:
                    return False
                else:
                    found = True

                index_bigger += 1
            else:
                index_smaller += 1
                index_bigger += 1

        return True
            

            
s = Solution()
result = s.check_one_away("PALE", "BAKE")
print(result)


        



