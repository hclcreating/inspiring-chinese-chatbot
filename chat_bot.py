from separate_and_choose_input import SeparateAndChooseInput as sep
import json
import numpy.random as random


# load dictionary of separated responses
with open("response_dict.json") as f:
    response_dict = json.load(f)

# load responses to a list
with open("all_sentences/responses.txt") as f:
    response_list = f.readlines()

is_going = True
while is_going:
    input_sentence = input("我想說...\n")
    try:
        sep.pickMeaningfulWord(input_sentence) in response_dict
        print(
            "Bot:\n",
            response_list[
                random.choice(response_dict[sep.pickMeaningfulWord(input_sentence)])
            ].strip(),
        )
    except Exception:
        print("Bot:\n加油！")
