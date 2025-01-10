from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        from collections import Counter
        max_counts = Counter()
        for word2 in words2:
            word2_counts = Counter(word2)
            for char, count in word2_counts.items():
                max_counts[char] = max(max_counts[char], count)

        universal_words = []
        for word1 in words1:
            word1_counts = Counter(word1)
            if all(word1_counts[char] >= count for char, count in max_counts.items()):
                universal_words.append(word1)

        return universal_words

if __name__ == "__main__":
    solution = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["lo", "eo"]
    print(solution.wordSubsets(words1, words2))  # ["google","leetcode"]