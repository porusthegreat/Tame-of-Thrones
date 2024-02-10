from collections import Counter


class Count:

    def __init__(self, word):
        self.word = word

    def count_letters(self):
        return Counter(self.word)
