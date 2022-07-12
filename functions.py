from random import *
from words_list import *


# random word from words list
def random_word_func():
    return choice(words)


# create hidden word
def hidden_word_func(random_word):
    hidden_word = ""
    for i in range(len(random_word)):
        hidden_word += "_"
    return hidden_word





