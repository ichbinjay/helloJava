class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        word_dict = {}
        max_count = 0

        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

        for word in words:
            reversed_word = word[::-1]
            if reversed_word in word_dict:
                max_count = max(max_count, word_dict[reversed_word])

        return max_count
    