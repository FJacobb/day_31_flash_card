import random

import pandas

class Word:
    def __init__(self):
        self.data = pandas.read_csv("data/french_words.csv")
        self.random_word()
    def random_word(self):
        self.french = self.data.French.to_list()
        self.word_in_french = random.choice(self.french)
        self.word_in_english = "".join(self.data[self.data.French == self.word_in_french].English.values)

    def right(self):
        self.french.remove(self.word_in_french)
        self.random_word()
    def wrong(self):
        self.random_word()


d = Word()
d.random_word()
d.right()