from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universal_words = []
        for word1 in words1:
            for word2 in words2:
                if not self.is_subset(word1, word2):
                    break
            else:
                universal_words.append(word1)
        return universal_words

    def is_subset(self, word1: str, word2: str) -> bool:
        for char in word2:
            if word2.count(char) > word1.count(char):
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["lo", "eo"]
    print(solution.wordSubsets(words1, words2))  # ["google","leetcode"]