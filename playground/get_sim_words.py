
from back.utils import load_fasttext_model
from threading import Semaphore
import time
from back.utils import similar_by_word
import json


def main():
    fasttext_model = load_fasttext_model()
    # https://stackoverflow.com/a/43067907
    sims = similar_by_word(fasttext_model, "zebra", 10)

    print(json.dumps(sims))


if __name__ == '__main__':
    main()
