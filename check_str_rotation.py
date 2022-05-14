class Solution:
    def is_rotation(self, word1: str, word2: str):
        if len(word1) != len(word2):
            return False

        s = word1 + word2
        return self._is_substring(s, word2)

    def _is_substring(self, word1, word2) -> True:
        for i in range(len(word1)):

            j = 1
            while j <= len(word2):
                print('verifying j = ', j, word1[i:i+j], word2[:j], word1[i:i+j] == word2[:j])
                if word1[i:i+j] == word2[:j]:
                    j += 1
                else:
                    
                    break

                if j > 2:
                    return True

        return False

s = Solution()
r = s.is_rotation("thiago", "iagoth")
print(r)