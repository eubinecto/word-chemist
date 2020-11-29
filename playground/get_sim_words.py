
from back.utils import load_fasttext_model
from threading import Semaphore
import time


def main():
    fasttext_model = load_fasttext_model()
    # https://stackoverflow.com/a/43067907
    fasttext_model.vectors_norm = fasttext_model.vectors  # prevent recalc of normed vectors
    print("loading similar words..")
    start = time.time()
    sims = fasttext_model.similar_by_word(word="eagle", topn=5)
    print(sims)
    end = time.time()
    print("elapsed:",  str(end - start))
    start = time.time()
    sims = fasttext_model.similar_by_word(word="transfer")
    print(sims)
    end = time.time()
    print("elapsed:", str(end - start))
    # Semaphore(0).acquire()  # just hang before being killed


if __name__ == '__main__':
    main()
