from typing_extensions import Self
import jieba
import numpy.random as random
import json

with open("response_dict.json") as f:
    response_dict = json.load(f)

no_sence_words = []
with open("all_sentences/no_sence_word_list.txt") as f:
    no_sence = f.readlines()
    for word in no_sence:
        no_sence_words.append(word.strip())


class SeparateAndChooseInput:
    def __init__(self):
        pass

    def pickMeaningfulWord(self, input):
        """
        separate input words, delete words with length less than 2, and randomly choose one of the left words
        """
        words = jieba.cut(input, cut_all=False)
        sep_input = []
        for word in words:
            if word in no_sence_words:
                pass
            else:
                sep_input.append(word)
        for inp in sep_input:
            if inp in response_dict:
                return inp
            else:
                pass
        return random.choice(sep_input)
