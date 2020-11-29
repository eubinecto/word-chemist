from back.config import MOST_FREQ_WORDS_TXT, CHOICES_TXT_PATH
from back.utils import STOP_WORDS
import random


def main():
    # filter out stopwords!
    choices = list()
    with open(MOST_FREQ_WORDS_TXT, 'r') as fh:
        for line in fh:
            word = line.split("\t")[1]
            if "or" in word:
                continue
            if word in STOP_WORDS:
                continue
            choices.append(word.strip())
    # just get 1000 of the choices
    choices = random.sample(choices, 1000)

    with open(CHOICES_TXT_PATH, 'w') as fh:
        for choice in choices:
            fh.write(choice + "\n")


if __name__ == '__main__':
    main()

