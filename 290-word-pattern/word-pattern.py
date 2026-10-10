
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = {}
        reverse_mapping = {}

        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]

            if letter in mapping:
                if mapping[letter] != word:
                    return False
            else:
                mapping[letter] = word

            if word in reverse_mapping:
                if reverse_mapping[word] != letter:
                    return False
            else:
                reverse_mapping[word] = letter

        return True

        